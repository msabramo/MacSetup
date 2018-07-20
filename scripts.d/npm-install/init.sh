#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

xargs -t npm install -g < $DIR/npm-install-packages.txt
