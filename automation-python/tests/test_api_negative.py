import requests

BASE_URL = "http://localhost:8000"


def test_unauthorized_access():
    r = requests.get(f"{BASE_URL}/transactions/")
    assert r.status_code == 401

def test_create_transaction_without_token():
    r = requests.post(
        f"{BASE_URL}/transactions/",
        json={
            "title": "Test",
            "amount": 100,
            "type": "expense",
            "category_id": 1
        }
    )
    assert r.status_code == 401