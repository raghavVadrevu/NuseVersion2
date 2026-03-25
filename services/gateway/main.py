from fastapi import FastAPI

app = FastAPI(title="Gateway Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "gateway"}
