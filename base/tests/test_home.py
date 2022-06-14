from django.test import Client


#  Emular requisição HTTP
def test_status_code(client:Client):
    resp = client.get('/')
    assert resp.status_code == 200