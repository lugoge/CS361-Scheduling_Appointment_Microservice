from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_create_appointment():
    response = client.post("/appointments", json={
        "user_id": "test_user",
        "start_time": "2026-06-10T14:00:00",
        "end_time": "2026-06-10T15:00:00"
    })

    assert response.status_code == 200
    assert response.json()["user_id"] == "test_user"


def test_conflict():
    client.post("/appointments", json={
        "user_id": "test_user",
        "start_time": "2026-06-10T16:00:00",
        "end_time": "2026-06-10T17:00:00"
    })

    # Try conflicting one
    response = client.post("/appointments", json={
        "user_id": "test_user2",
        "start_time": "2026-06-10T16:30:00",
        "end_time": "2026-06-10T17:30:00"
    })

    assert response.status_code == 400
