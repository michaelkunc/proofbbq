import pytest

from proofbbq import app

@pytest.fixture
def client():
    app.config['TESTING'] == True
    client = app.test_client()
    yield client


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_cooks(client):
    resp = client.get('/cooks')
    assert resp.status_code == 200


@pytest.mark.xfail
def test_users(client):
    resp = client.get('/users')
    assert resp.status_code == 200

