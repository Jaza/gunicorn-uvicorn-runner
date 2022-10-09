from unittest.mock import patch

from gunicorn_uvicorn_runner.core import run_gunicorn_or_uvicorn


@patch("gunicorn_uvicorn_runner.core.multiprocessing")
@patch("gunicorn_uvicorn_runner.core.StandaloneApplication")
def test_run_gunicorn(mock_standalone_application, mock_multiprocessing):
    app_uri = "foo.main:app"
    web_host = "1.2.3.4"
    web_port = 8042
    reload = False
    mock_multiprocessing.cpu_count.return_value = 13
    expected_options = {
        "bind": f"{web_host}:{web_port}",
        "workers": 27,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }

    run_gunicorn_or_uvicorn(app_uri, web_host, web_port, reload)

    mock_standalone_application.assert_called_with(app_uri, expected_options)


@patch("gunicorn_uvicorn_runner.core.uvicorn")
def test_run_uvicorn(mock_uvicorn):
    app_uri = "foo.main:app"
    web_host = "1.2.3.4"
    web_port = 8042
    reload = True

    run_gunicorn_or_uvicorn(app_uri, web_host, web_port, reload)

    mock_uvicorn.run.assert_called_with(
        app_uri, host=web_host, port=web_port, reload=True
    )
