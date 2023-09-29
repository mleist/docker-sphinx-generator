# docker-sphinx-generator

Creates PDF documents as well as HTML pages from complex Markdown texts.

## Build docker image

in ./image

```bash
$ docker build --tag=docker-sphinx-generator:0.1 .
```

## Run docker image

in ./example

```bash
$ docker run -it --rm -v "$(pwd):/docs" docker-sphinx-generator:0.1 make latexpdf
```

## The result

The first demo run produces this [PDF document](https://github.com/mleist/docker-sphinx-generator/blob/4647c7cd805068f16605d87d7f898f55497b137b/example/acme_example.pdf)
