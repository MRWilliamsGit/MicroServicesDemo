from fastapi import FastAPI
from fastapi.testclient import TestClient
from heythere import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello There Friend!"}

def test_read_add():
    response = client.get("/adder/2/2")
    assert response.status_code == 200
    assert response.json() == {"total": 4}
    
def test_read_name():
    response = client.get("/hey/Angel")
    assert response.status_code == 200
    assert response.json() == {"message": "You have a nice name, Angel!"}