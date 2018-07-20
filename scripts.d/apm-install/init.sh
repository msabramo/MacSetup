#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

( set -x; apm install --packages-file $DIR/apm-install-packages.txt )
