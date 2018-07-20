#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for f in $DIR/dotfiles/.*; do
    echo cp -pr $f ~
    cp -pr $f ~
done
