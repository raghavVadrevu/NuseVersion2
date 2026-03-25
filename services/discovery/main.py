from fastapi import FastAPI

from .routers import router as discovery_router


app = FastAPI(title="NUSE Discovery Service")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "nuse-discovery-service"}


app.include_router(discovery_router)
