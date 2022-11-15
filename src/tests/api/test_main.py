from http import HTTPStatus
from fastapi.testclient import TestClient


def test_main_page(client: TestClient):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
