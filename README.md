# hello-postmodern-python-tooling

A small project to play with the "postmodern" and simpler toolchain outlined in [^1].

## Setup

Install [rye](https://rye.astral.sh/):

```shell
% curl -sSf https://rye.astral.sh/get | bash
```

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

## References

[^1]: [Chris Arderne (2024), Beyond Hypermodern: Python is easy now](https://rdrn.me/postmodern-python/)
