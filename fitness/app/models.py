from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    dateTime = Column(DateTime, nullable=False)
    instructor = Column(String(100), nullable=False)
    availableSlots = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    client_name = Column(String(100), nullable=False)
    client_email = Column(String(100), nullable=False)

    fitness_class = relationship("Class", back_populates="bookings")
