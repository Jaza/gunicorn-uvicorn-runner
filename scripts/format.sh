#!/bin/bash
$HOME/.local/bin/poetry run autoflake \
    --remove-all-unused-imports \
    --recursive \
    --remove-unused-variables \
    --in-place \
    gunicorn_uvicorn_runner tests
$HOME/.local/bin/poetry run black gunicorn_uvicorn_runner tests
$HOME/.local/bin/poetry run isort gunicorn_uvicorn_runner tests
