#!/bin/sh

set -e

apk --update add --no-cache python3

pip3 install --upgrade pip
pip3 install -r requirements.txt
