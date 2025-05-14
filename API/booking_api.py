import requests

from config.config import BASE_URL, BOOKING_ENDPOINT


class BookingAPI:

    def create_booking(self, payload):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        return response

    def get_booking_by_id(self, booking_id):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}/{booking_id}"
        response = requests.get(url)

        return response

    def delete_booking(self, booking_id, token ):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}/{booking_id}"
        headers = {
            'Content-Type': 'application/json',
                   'Cookie': f"token={token}"
        }

        return requests.delete(url, headers=headers)

    def update_booking(self, booking_id, payload, token):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}/{booking_id}"
        headers = {
            'Content-Type': 'application/json',
                   'Cookie': f"token={token}"
        }
        return requests.patch(url, json=payload, headers=headers)