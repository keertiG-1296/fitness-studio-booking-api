from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/book", response_model=schemas.BookingResponse)
def book(booking_data: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.book_class(db, booking_data)

@router.get("/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
