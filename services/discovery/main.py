import os
import sys

from fastapi import FastAPI

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from routers.discovery import router as discovery_router

app = FastAPI(title="nuse-discovery-service")

app.include_router(discovery_router)


@app.get("/health")
def health():
    print("🚀 Starting Discovery Service...")
    return {"status": "ok", "service": "nuse-discovery-service"}