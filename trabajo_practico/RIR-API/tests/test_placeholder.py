from app.main import app
from fastapi.testclient import TestClient

# Crear el cliente de pruebas de FastAPI
client = TestClient(app)


# Test para verificar el endpoint principal ("/")
def test_read_root():
    response = client.get("/")  # Hacer una solicitud GET al endpoint "/"
    assert response.status_code == 200  # Verificar que el código de estado sea 200
    assert response.json() == {
        "message": "Bienvenido a la API RIR"
    }  # Verificar el contenido de la respuesta
