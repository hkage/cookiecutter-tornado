{%- set python_versions = cookiecutter.python_versions.split(",") -%}
FROM python:{{ python_versions[-1] }}-alpine

LABEL maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.email }}>"

USER root

WORKDIR /app
ADD . /app/

RUN apk --update add --no-cache git \
    && pip install wheel \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/*
