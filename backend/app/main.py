from fastapi import FastAPI

app = FastAPI(title="Café Editorial")

@app.get("/api/health")
def health():
    return {"status": "ok"}
