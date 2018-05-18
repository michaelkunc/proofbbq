import pytest

from proofbbq import app

@pytest.fixture
def client():
    app.config['TESTING'] == True
    client = app.test_client()
    yield client

def test_index(client):
    resp = client.get('/')
    assert resp.data == b'Hello World!'

