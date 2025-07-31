# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, crud, database
from .crud import ItemCreate

app = FastAPI()

# Allow all origins (for development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/")
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
