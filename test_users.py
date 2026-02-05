import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404
    