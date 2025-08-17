import pytest
import json
from routes import *


@pytest.fixture
def client():
    a = create_app()
    with a.test_client() as client:
        yield client

#基本的にAPIはServiceの中にあるMethodのみを返す
#今あるのは def lookup_word(self, surface_form: str):のみ

def test_hello(client):
    rv = client.get("/hello")
    assert rv.status_code == 200
    assert b"Hello, World!" in rv.data



def test_lookup_success(client):
    rv = client.get("/entries/revoked")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data.get("lemma_form") == "revoke"


def test_lookup_fail(client):
    rv = client.get("/entries/unknown")
    data = rv.get_json()
    assert "error" in data

