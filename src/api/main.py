from fastapi import FastAPI

app = FastAPI(
    title="HeatWatch API",
    description="Urban heat island analysis for climate adaptation",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"status": "ok", "project": "HeatWatch", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"healthy": True}
