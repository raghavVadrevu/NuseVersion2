from fastapi import FastAPI

app = FastAPI(title="Extraction Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "extraction"}
