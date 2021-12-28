# pylint: disable=redefined-outer-name
import pytest
from approvaltests.approvals import verify
from flask_app import flask_app


@pytest.fixture
def http_client():
    flask_app.testing = True
    return flask_app.test_client()


def test_default_route(http_client):
    response = http_client.get('/')
    parsed_body = response.data.decode('utf-8')

    verify(parsed_body)
