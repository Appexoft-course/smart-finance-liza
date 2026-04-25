import requests

BASE_URL = "http://localhost:8000"


def test_forecast(auth_headers):
    start = requests.post(
        f"{BASE_URL}/forecast/expenses",
        headers=auth_headers
    )

    assert start.status_code == 200

    task_id = start.json()["task_id"]

    result = requests.get(
        f"{BASE_URL}/forecast/expenses/{task_id}",
        headers=auth_headers
    )

    assert result.status_code == 200
    assert "status" in result.json()