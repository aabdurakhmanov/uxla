from fastapi.testclient import TestClient
from agent.main import app

client = TestClient(app)

def test_index_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "MySite" in response.text  # title chiqyaptimi?

def test_about_page():
    response = client.get("/about")
    assert response.status_code == 200
    assert "Adi" in response.text  # about page’da ism chiqyaptimi?

def test_shutdown_route():
    response = client.get("/shutdown")
    assert response.status_code == 200
    assert response.json()["status"] == "Shutting down..."

def test_restart_route():
    response = client.get("/restart")
    assert response.status_code == 200
    assert response.json()["status"] == "Restarting..."
