from app.core.security import hash_password, verify_password


def test_hash_password():
    password = "test1234"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True


def test_verify_wrong_password():
    password = "test1234"
    hashed = hash_password(password)

    assert verify_password("wrong_password", hashed) is False