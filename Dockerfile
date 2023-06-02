FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry install --no-interaction --no-ansi

COPY ./app .