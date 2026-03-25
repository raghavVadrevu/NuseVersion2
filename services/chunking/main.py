from fastapi import FastAPI

app = FastAPI(title="Chunking Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "chunking"}
