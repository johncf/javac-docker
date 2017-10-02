# java-docker

Compile and run a single Java source file using a docker image.

This is intended to be used behind a web-based Java compiler service.

## Basic Usage

- Put your source code in `workdir/source`
- Populate `workdir/stdin` if needed.
- Run `java-docker.sh`

Wait for the process to exit; you'll find `workdir/stdout` and `workdir/stderr`
populated with the output from the Java program. Errors and warnings emitted by
`javac` will be redirected to `workdir/stderr-javac`.
