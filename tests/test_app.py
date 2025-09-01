# tests/test_app.py
from app.app import app
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_home():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["message"] == "Hello from GitHub Actions CI/CD with Python!"

def test_addition():
    client = app.test_client()
    response = client.get("/add/3/4")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["result"] == 7
