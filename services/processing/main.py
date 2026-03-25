from fastapi import FastAPI

app = FastAPI(title="Processing Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "processing"}
