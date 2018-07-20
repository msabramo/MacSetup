#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

xargs -t brew cask install < $DIR/brew-cask-install-packages.txt
