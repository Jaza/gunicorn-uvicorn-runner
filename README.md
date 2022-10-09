# gunicorn-uvicorn-runner

Run either gunicorn or uvicorn depending on whether reloading is needed.


## Getting started

1. Install a recent Python 3.x version (if you don't already have one).
2. Create a Python web project (if you don't already have one) - for example a [FastAPI](https://fastapi.tiangolo.com/) based project.
3. Install `gunicorn-uvicorn-runner` as a dependency using [Poetry](https://python-poetry.org/), pip, or similar:
   ```sh
   poetry add gunicorn-uvicorn-runner
   ```
4. Use it:
   ```python
   from gunicorn_uvicorn_runner import run_gunicorn_or_uvicorn


   if __name__ == "__main__":
       run_gunicorn_or_uvicorn("myproject.main:app", "1.2.3.4", 8042, True)
   ```


## Developing

To clone the repo:

```sh
git clone git@github.com:Jaza/gunicorn-uvicorn-runner.git
```

To automatically fix code style issues:

```sh
./scripts/format.sh
```

To verify code style and static typing:

```sh
./scripts/verify.sh
```

To run tests:

```sh
./scripts/test.sh
```


## Building

To build the library:

```sh
poetry build
```


Built by [Seertech](https://www.seertechsolutions.com/).
