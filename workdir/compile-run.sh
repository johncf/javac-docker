#!/bin/sh

set -e

CNAME=$(cat classname)

set -x

javac $CNAME.java 2>stderr-javac
java $CNAME <stdin >stdout 2>stderr
