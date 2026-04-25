import uuid
import requests

BASE_URL = "http://localhost:8000"


def test_register_login_and_me():
    unique = str(uuid.uuid4())[:8]

    user = {
        "username": f"api_user_{unique}",
        "email": f"api_user_{unique}@mail.com",
        "password": "1234",
    }

    register_response = requests.post(f"{BASE_URL}/auth/register", json=user)
    assert register_response.status_code in (200, 201)

    login_response = requests.post(f"{BASE_URL}/auth/login", json=user)
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    me_response = requests.get(
        f"{BASE_URL}/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert me_response.status_code == 200
    assert me_response.json()["username"] == user["username"]