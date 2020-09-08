#! /bin/sh
set -e
find . -name '*.py' -exec pyupgrade --py36-plus {} +
python -m black tests aioeafm
python -m isort tests aioeafm
python -m black tests aioeafm --check --diff
python -m flake8 tests aioeafm
python -m pylint tests aioeafm
python -m pytest
