#!/bin/sh

set -e

apt-get update

APT_PACKAGES="
python-pip
python-dev
python3-pycurl
libcurl4-openssl-dev
"

apt-get -y install $APT_PACKAGES
