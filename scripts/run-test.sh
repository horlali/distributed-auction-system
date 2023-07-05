#!/bin/sh

cd $(dirname $0)/..

poetry run coverage run -m pytest ${ARGS}
poetry run coverage report -m
