# 📄 tests/test_api.py (수정 후 전체 복붙용)
from fastapi.testclient import TestClient
from src.routes.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SNS Auto Project API Root"}


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.0.0"}
