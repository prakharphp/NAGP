# app/crud.py
from sqlalchemy.orm import Session
from . import models
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str = ""
    price: float
    quantity: int

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session):
    return db.query(models.Item).all()

def create_item(db: Session, item: ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    for field, value in item.dict().items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
