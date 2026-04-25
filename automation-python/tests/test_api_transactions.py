import uuid
import requests

BASE_URL = "http://localhost:8000"


def test_create_transaction(auth_headers):
    unique = str(uuid.uuid4())[:8]

    category_response = requests.post(
        f"{BASE_URL}/categories/",
        json={"name": f"Food_{unique}"},
        headers=auth_headers,
    )

    assert category_response.status_code in (200, 201)

    category_id = category_response.json()["id"]

    transaction_response = requests.post(
        f"{BASE_URL}/transactions/",
        json={
            "title": "Lunch",
            "amount": 200,
            "type": "expense",
            "category_id": category_id,
        },
        headers=auth_headers,
    )

    assert transaction_response.status_code in (200, 201)
    assert transaction_response.json()["title"] == "Lunch"
    assert transaction_response.json()["amount"] == 200
    assert transaction_response.json()["type"] == "expense"


def test_get_transactions(auth_headers):
    response = requests.get(
        f"{BASE_URL}/transactions/",
        headers=auth_headers,
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)