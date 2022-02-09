from fastapi import FastAPI
from fastapi.testclient import TestClient
from heythere import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello There Friend!"}

def test_read_adder():
    response = client.get("/adder/2/2")
    assert response.status_code == 200
    assert response.json() == {"total": 4}