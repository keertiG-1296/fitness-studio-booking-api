from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from datetime import datetime
import pytz

def create_class(db: Session, class_data: schemas.ClassCreate):
    ist = pytz.timezone("Asia/Kolkata")
    utc = pytz.utc

    
    ist_time = ist.localize(class_data.dateTime)
    utc_time = ist_time.astimezone(utc)

    new_class = models.Class(
        name=class_data.name,
        dateTime=utc_time,
        instructor=class_data.instructor,
        availableSlots=class_data.availableSlots
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    print("Class created in UTC:", new_class.dateTime)
    return new_class


def get_all_classes(db: Session):
    return db.query(models.Class).all()



def book_class(db: Session, booking_data: schemas.BookingCreate):
    fitness_class = db.query(models.Class).filter(models.Class.id == booking_data.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    if fitness_class.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    fitness_class.availableSlots -= 1
    booking = models.Booking(**booking_data.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_email(db: Session, email: str):
    print("Searching bookings for email:", email)
    results = db.query(models.Booking).filter(models.Booking.client_email == email).all()
    print("Results:", results)
    return results

    
