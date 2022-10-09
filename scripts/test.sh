#!/bin/bash
set -e

$HOME/.local/bin/poetry run pytest \
  --cov=gunicorn_uvicorn_runner \
  --cov=tests \
  --cov-fail-under=100 \
  --cov-report=term-missing \
  tests

set +e
