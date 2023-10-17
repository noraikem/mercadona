from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    category = Column(String)

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    discount_percentage = Column(Float)
