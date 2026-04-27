from fastapi import APIRouter

# Crear un router de FastAPI
router = APIRouter()


# Definir el endpoint /health
@router.get("/health")
def read_health():
    return {"message": "La API está funcionando correctamente."}
