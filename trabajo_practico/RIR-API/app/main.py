from fastapi import FastAPI

from app.routers.health import router as health_router  # Importa el router del health

app = FastAPI()

# Incluye el router de health
app.include_router(health_router)


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API RIR"}
