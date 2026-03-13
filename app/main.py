import os

from fastapi import FastAPI
from app.api.routes import router
from app.models.schemas import HealthResponse, RootResponse

app = FastAPI(
    title="Elective Recommendation API",
    version="1.0.0",
)

app.include_router(router)

@app.get("/", response_model=RootResponse)
def root():
    return {"message": "Elective Recommendation API"}


@app.get("/healthz", response_model=HealthResponse)
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)