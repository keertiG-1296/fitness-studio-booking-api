from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ClassResponse)
def create_class(class_data: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, class_data)

@router.get("/", response_model=list[schemas.ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    return crud.get_all_classes(db)
