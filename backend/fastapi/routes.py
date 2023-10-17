from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

@router.get("/products/{product_id}")
def read_product(product_id: int):
    return {"product_id": product_id, "product_name": "Example Product"}
