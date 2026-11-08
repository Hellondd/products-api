from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=80)
    price: int = Field(ge=0)
    in_stock: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    """PUT = полная замена, поэтому поля те же, что при создании."""


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int