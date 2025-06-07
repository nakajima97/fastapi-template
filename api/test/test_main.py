from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_dummy():
    response = client.get("/")
    assert response.status_code == 200


def test_health_check_db():
    response = client.get("/api/v1/health/db")
    # DBが起動していない場合は503エラーが想定される
    assert response.status_code in [200, 503]
