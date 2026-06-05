# CS361-Scheduling_Appointment_Microservice
Microservice to schedule and assign appointments.

## Overview
This Microservice provides functionality for creating, managing, and cancleing sheduled appointments. It allows users to reserve tiem slots for events while preventing overlapping (double-booked) appointments.

Built with **FASTAPI** and **SQLite**, this service is lightweight and easy to run locally.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd scheduler
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```
Then active the environment

**Mac/Linux:**
``` bash
source venv/bin/activate
```
**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Microservice
```bash
uvicorn app.main:app --reload
```
Success when message 
```
Uvicorn running on http://127.0.0.1:8000
```