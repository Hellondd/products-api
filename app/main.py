from fastapi import FastAPI

from app.database import Base, engine
from app import models  # noqa: F401
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Products API", version="1.0.0")
app.include_router(products.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok"}