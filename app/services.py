from sqlalchemy.orm import Session
from app import models

def has_conflict(db: Session, start_time, end_time):
    return db.query(models.Appointment).filter(
        models.Appointment.start_time < end_time,
        models.Appointment.end_time > start_time,
        models.Appointment.status == "scheduled"
    ).first() is not None

def create_appointment(db: Session, appointment):
    if appointment.start_time >= appointment.end_time:
        raise ValueError("Invalid time range")
    
    if has_conflict(db, appointment.start_time, appointment.end_time):
        raise ValueError("Time slot already booked")
    
    db_appt = models.Appointment(
        user_id=appointment.user_id,
        start_time=appointment.start_time,
        end_time=appointment.end_time
    )

    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)

    return db_appt