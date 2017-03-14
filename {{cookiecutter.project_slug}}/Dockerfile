FROM phusion/baseimage:0.9.19

MAINTAINER {{ cookiecutter.author_name }} "{{ cookiecutter.email }}"

USER root

ENV PYTHON_VERSION 2.7

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential openssh-client git git-core python-pip procps net-tools wget unzip python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python-distribute \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ADD . /app/

RUN pip install wheel \
    && pip install -r requirements.txt
RUN chown -R www-data: /app
