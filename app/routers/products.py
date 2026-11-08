from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    if crud.get_product_by_name(db, data.name):
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "Product with this name already exists",
        )
    return crud.create_product(db, data)