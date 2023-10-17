from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name: str
    description: str
    price: float
    image: str
    category: str

class ProductCreate(ProductBase):
    pass

class PromotionBase(BaseModel):
    product_id: int
    start_date: date
    end_date: date
    discount_percentage: float
