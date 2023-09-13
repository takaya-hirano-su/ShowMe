FROM python:3.11.5-alpine

WORKDIR /app

ENV PYTHONPATH /app

RUN apk update && apk add --no-cache musl-dev gcc make g++ file libpq-dev

COPY /app/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel

ENV PYTHONPATH /app

RUN pip install -r requirements.txt
