#!/bin/sh

set -e

CNAME=$(cat classname)

javac $CNAME.java 2>stderr-javac

set +e

timeout -t2 java $CNAME <stdin >stdout 2>stderr
echo "Exited with code: $?"
