import pytest
from app import app

@pytest.fixture
def client():
  app.config.update(TESTING=True)
  return app.test_client()


def test_home(client):
  response = client.get("/")
  assert response.status_code == 200
  data = response.get_json()
  assert data["message"] == "CI DEMO API is running"

def test_health(client):
  response = client.get("/health")
  assert response.status_code == 200
  assert response.get_json() == {"status":"ok"}
