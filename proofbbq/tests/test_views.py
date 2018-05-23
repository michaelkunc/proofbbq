import pytest

from proofbbq import app


@pytest.fixture(scope="session")
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


@pytest.mark.parametrize("endpoint,status_code", [("/", 200), ("/cooks", 200), ("/cooks/1", 200), ("/grills", 200)])
def test_responses(client, endpoint, status_code):
    resp = client.get(endpoint)
    assert resp.status_code == status_code


@pytest.mark.xfail
def test_users(client):
    resp = client.get("/users")
    assert resp.status_code == 200
