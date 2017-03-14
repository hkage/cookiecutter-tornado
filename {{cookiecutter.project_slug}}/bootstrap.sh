#!/bin/sh

set -e

apt-get update

APT_PACKAGES="
python-pip
python-dev
"

apt-get -y install $APT_PACKAGES

pip install -r requirements.txt
