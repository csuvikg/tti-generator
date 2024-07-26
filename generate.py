from json import loads
from random import choice
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--grade', action='store_true')
args = parser.parse_args()

grade = args.grade

with open('questions.json') as f:
    questions = loads(f.read())
    for question in questions:
        print(f"- {question['category']}: {choice(question['questions'])}")
        if grade:
            print("  - +:\n  - -:\n  - result:")
