from fastapi import FastAPI

app = FastAPI(title="Retrieval Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "retrieval"}
