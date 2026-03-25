from fastapi import FastAPI

app = FastAPI(title="Acquisition Service")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "acquisition"}
