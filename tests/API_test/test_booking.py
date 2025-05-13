import pytest
from API.booking_api import BookingAPI
from utils.payloader_builder import BookingPayloadBuilder
from API.auth_api import AuthApi

@pytest.fixture(scope='module')
def auth_token():
    auth_api = AuthApi()
    response = auth_api.create_token()

    assert response.status_code == 200
    return response.json()['token']

def test_create_booking_positive():
    booking_api = BookingAPI()

    payload = BookingPayloadBuilder() \
        .set_firstname("SANYA") \
        .set_lastname("OJRA") \
        .set_totalprice(666) \
        .set_depositpaid(True) \
        .set_checkin("2025-04-01") \
        .set_checkout("2025-04-05") \
        .set_additional_needs("Espresso") \
        .build()

    response = booking_api.creat_booking(payload)
    assert response.status_code == 200
    assert "bookingid" in response.json()


def test_create_booking_negative_miss_req_fds():
    booking_api = BookingAPI()

    #Нету обязательных полей
    payload = {}

    response = booking_api.creat_booking(payload)

    assert response.status_code == 500