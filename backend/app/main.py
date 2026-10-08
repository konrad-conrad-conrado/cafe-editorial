from fastapi import FastAPI
from app.modules.editorial.router import router
app = FastAPI(title="Café Editorial")
app.include_router(router, prefix="/api")
@app.get("/api/health")
def health():
    return {"status": "ok"}
