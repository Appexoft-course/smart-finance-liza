import pytest
import requests
import uuid

BASE_URL = "http://localhost:8000"


@pytest.fixture
def user_data():
    unique = str(uuid.uuid4())[:8]
    return {
        "username": f"user_{unique}",
        "email": f"{unique}@mail.com",
        "password": "1234"
    }


@pytest.fixture
def token(user_data):
    # register
    requests.post(f"{BASE_URL}/auth/register", json=user_data)

    # login
    r = requests.post(f"{BASE_URL}/auth/login", json=user_data)
    return r.json()["access_token"]


@pytest.fixture
def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }