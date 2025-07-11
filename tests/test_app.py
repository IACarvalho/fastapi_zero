from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retorna_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello World'}
