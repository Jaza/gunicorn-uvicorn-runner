#!/bin/bash
set -e

$HOME/.local/bin/poetry run black gunicorn_uvicorn_runner tests --check
$HOME/.local/bin/poetry run isort --check-only gunicorn_uvicorn_runner tests
$HOME/.local/bin/poetry run flake8 gunicorn_uvicorn_runner tests
$HOME/.local/bin/poetry run mypy gunicorn_uvicorn_runner tests
$HOME/.local/bin/poetry run bandit -r gunicorn_uvicorn_runner tests

set +e
