FROM debian:stable

MAINTAINER {{ cookiecutter.author_name }} "{{ cookiecutter.email }}"

USER root

# Link the project directory
ADD . /app

# Set environment variables
ENV PYTHON_VERSION 2.7

# Install basic requirements
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends build-essential openssh-client git git-core python-pip procps net-tools wget unzip python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python-distribute

# Install the requirements and run the application
RUN (cd /app && python setup.py install)
#CMD (cd /app && python run.py --port=8000 --logging=debug)

RUN chown -R www-data: /app

CMD ["python", "/app/run.py"]

EXPOSE 8000
