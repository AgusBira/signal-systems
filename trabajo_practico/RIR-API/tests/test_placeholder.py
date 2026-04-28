from app.main import app
from fastapi.testclient import TestClient

# Crear el cliente de pruebas de FastAPI
client = TestClient(app)


# Test para verificar el endpoint principal ("/")
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
