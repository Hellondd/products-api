from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int) -> Product | None:
    return db.get(Product, product_id)


def get_product_by_name(db: Session, name: str) -> Product | None:
    return db.scalar(select(Product).where(Product.name == name))


def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
def list_products(
    db: Session,
    min_price: int | None = None,
    max_price: int | None = None,
    in_stock: bool | None = None,
) -> list[Product]:
    stmt = select(Product)
    if min_price is not None:
        stmt = stmt.where(Product.price >= min_price)
    if max_price is not None:
        stmt = stmt.where(Product.price <= max_price)
    if in_stock is not None:
        stmt = stmt.where(Product.in_stock == in_stock)
    return list(db.scalars(stmt.order_by(Product.id)))

def update_product(db: Session, product: Product, data: ProductUpdate) -> Product:
    for field, value in data.model_dump().items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product