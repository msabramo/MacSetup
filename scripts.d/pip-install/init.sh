#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

xargs -t pip install < $DIR/pip-install-packages.txt
