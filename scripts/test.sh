#! /bin/sh

set -e

isort -rc aioeafm tests
black aioeafm tests
flake8 aioeafm tests
mypy aioeafm
pylint aioeafm tests

coverage run -m pytest tests/

