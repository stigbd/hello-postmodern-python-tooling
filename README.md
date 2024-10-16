# hello-postmodern-python-tooling

A small project to play with the "postmodern" and simpler toolchain outlined in [^1].


## Install and test Rye

Install [rye](https://rye.astral.sh/):

```shell
% curl -sSf https://rye.astral.sh/get | bash
```

Test the installation

```shell
% rye --version
```

Create a hello-world project in a new directory and run it:

```shell
% rye init --script hello-world
% cd hello-world
% rye sync
% rye run hello-world
Hello from hello-world!
```

Update rye itself

```shell
% rye self update
```

## Set and run # hello-postmodern-python-tooling

The following assumes you are in the root of the project.

Create lockfiles and install Python + dependencies:

```shell
% rye sync
```

## Run formatting

```shell
% rye fmt
```

## Run linter

```shell
% rye lint --fix
```

## Run typechecking

```shell
% rye check
```

## Run the tests

```shell
% rye test
```

## Run all of the above

```shell
% rye run all
```

## Run the server in dev mode

```shell
% rye run fastapi dev
```

To see the API-documentation, go to <http://127.0.0.1:8000/docs>

## Run the server in docker

```shell
% docker build -t myimage .
% docker run --name mycontainer -p 8000:80 myimage
```

## Update dependencies

```shell
% rye sync --update-all
```

## References

[^1]: [Chris Arderne (2024), Beyond Hypermodern: Python is easy now](https://rdrn.me/postmodern-python/)
