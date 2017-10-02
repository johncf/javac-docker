#!/bin/sh

set -e

if [ -z "$1" ]; then
    WORKDIR="$PWD/workdir"
else
    WORKDIR=`cd "$1" && pwd`
fi

if [ -f "$WORKDIR/source" ]; then
    CLASSNAME=$(python3 preprocess.py "$WORKDIR"/source)
    mv "$WORKDIR"/source "$WORKDIR"/"$CLASSNAME".java
    echo "$CLASSNAME" > "$WORKDIR"/classname
    touch "$WORKDIR"/stdin
fi

cp compile-run.sh "$WORKDIR"/compile-run.sh
sudo docker run --memory=128M --rm -v "$WORKDIR":/myapp -w /myapp openjdk:8-alpine sh compile-run.sh
