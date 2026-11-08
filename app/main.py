from fastapi import FastAPI

app = FastAPI(title="Products API", version="1.0.0")


@app.get("/", tags=["health"])
def root():
    return {"status": "ok"}