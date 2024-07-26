FROM python:3.9.19-slim

WORKDIR /app

COPY . .

ENTRYPOINT [ "python3", "generate.py" ]