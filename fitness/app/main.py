from fastapi import FastAPI
from app.routes import class_routes, booking_routes
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Fitness Class Booking API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(class_routes.router, prefix="/classes", tags=["Classes"])
app.include_router(booking_routes.router, tags=["Bookings"])

@app.get("/")
def root():
    return {"message": "Fitness Booking API is running"}
