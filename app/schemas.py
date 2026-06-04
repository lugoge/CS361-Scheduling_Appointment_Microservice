from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    user_id: str
    start_time: datetime
    end_time: datetime

class AppointmentResponse(BaseModel):
    id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    status: str
    
    class Config:
        orm_mode = True