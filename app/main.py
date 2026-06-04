from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, schemas, services

app = FastAPI(title="Scheduling Microservice (SQLite)")

# Create tables automatically
Base.metadata.create_all(bind=engine)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create appointment
@app.post("/appointments", response_model=schemas.AppointmentResponse)
def create_appointment(appt: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    try:
        return services.create_appointment(db, appt)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

# Get appointments for a user
@app.get("/appointments/{user_id}")
def get_appointments(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.Appointment).filter(
        models.Appointment.user_id == user_id
    ).all()

# Cancel appointment
@app.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: str, db: Session = Depends(get_db)):
    appt = db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()

    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    appt.status = "canceled"
    db.commit()

    return {"message": "Appointment canceled"}