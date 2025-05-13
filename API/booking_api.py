from wsgiref import headers

import requests

from config.config import BASE_URL, BOOKING_ENDPOINT


class BookingAPI:

    def creat_booking(self, payload):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        return response

    def get_booking(self, payload, booking_id):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}/{booking_id}"
        response = requests.get(url)

        return response

    def delete_booking(self, booking_id, token ):
        url = f"{BASE_URL}{BOOKING_ENDPOINT}/{booking_id}"
        headers = {'Content-Type': 'application/json',
                   'Cookie': f"token={token}"}

        response = requests.delete(url, json=payload, headers=headers)
        return response

