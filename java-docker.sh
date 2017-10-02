#!/bin/sh

sudo docker run --memory=128M --rm -v "$PWD/workdir":/myapp -w /myapp openjdk:8-alpine sh compile-run.sh
