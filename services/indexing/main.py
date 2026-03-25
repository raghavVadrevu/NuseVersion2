from fastapi import FastAPI

app = FastAPI(title="Indexing Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "indexing"}
