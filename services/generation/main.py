from fastapi import FastAPI

app = FastAPI(title="Generation Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "generation"}
