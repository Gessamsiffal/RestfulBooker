import requests
from config.config import BASE_URL, AUTH_ENDPOINT


class AuthApi:
    def create_token(self):
        url = f"{BASE_URL}{AUTH_ENDPOINT}"
        payload = {
            "username": "admin",
            "password": "password123"
        }
        response = requests.post(url, json=payload)

        return response