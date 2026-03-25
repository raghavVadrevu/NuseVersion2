import os
import sys

from fastapi import FastAPI

# Add project root to path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from routers.discovery import router as discovery_router
from config import settings


app = FastAPI(title=settings.APP_NAME)

app.include_router(discovery_router)


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.APP_NAME}