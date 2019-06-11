FROM python:3.7-alpine

MAINTAINER {{ cookiecutter.author_name }} "{{ cookiecutter.email }}"

USER root

RUN apk --update add --no-cache git \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/*

WORKDIR /app
ADD . /app/

RUN pip install wheel \
    && pip install -r requirements.txt
RUN chown -R www-data: /app
