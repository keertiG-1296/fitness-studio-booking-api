from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

class ClassResponse(ClassCreate):
    id: int
    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    class Config:
        orm_mode = True