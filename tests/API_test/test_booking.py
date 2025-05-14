import pytest
import allure
from API.booking_api import BookingAPI
from utils.payloader_builder import BookingPayloadBuilder

from schemas.booking_response_schema import booking_response_schema
from utils.schema_validator import SchemaValidator


@allure.feature('Booking API')
class BaseBookingTest:
    @pytest.fixture(autouse=True)
    def init_setup(self, auth_token):
        self.booking_api = BookingAPI()
        self.token = auth_token
        self.create_booking = []

    def create_booking_for_test(self, payload=None):
        if payload is None:
            payload = BookingPayloadBuilder() \
                .set_firstname("Default") \
                .set_lastname("User") \
                .set_totalprice(123) \
                .set_depositpaid(True) \
                .set_checkin("2025-01-01") \
                .set_checkout("2025-01-02") \
                .set_additional_needs("Breakfast") \
                .build()

        response = self.booking_api.create_booking(payload)
        assert response.status_code == 200
        booking_id = response.json()['bookingid']
        self.create_booking.append(booking_id)
        return booking_id, response

    def teardown_method(self):
        for booking_id in self.create_booking:
            with allure.step(f'Удаление бронирования с ID: {booking_id}'):
                response = self.booking_api.delete_booking(booking_id, self.token)
                assert response.status_code in [201, 204], f"Не удалось удалить бронирование {booking_id}"



@pytest.mark.api
@pytest.mark.positive
@allure.feature('Booking API')
@allure.story('Позитивные тест-кейсы')
class TestBookingPositive(BaseBookingTest):

    @allure.title('Успешное создание бронирования')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_booking(self):
        payload = BookingPayloadBuilder() \
            .set_firstname("SANYA") \
            .set_lastname("OJRA") \
            .set_totalprice(666) \
            .set_depositpaid(True) \
            .set_checkin("2025-04-01") \
            .set_checkout("2025-04-05") \
            .set_additional_needs("Espresso") \
            .build()


        response = self.booking_api.create_booking(payload)
        assert response.status_code == 200
        resp_json = response.json()

        SchemaValidator.validate(resp_json, booking_response_schema)

    @allure.title('Частичное обновление бронирования')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_booking_partial(self):
        payload = BookingPayloadBuilder() \
            .set_firstname("Igor") \
            .set_lastname("Reo") \
            .set_totalprice(777) \
            .set_depositpaid(True) \
            .set_checkin("2025-05-01") \
            .set_checkout("2025-06-05") \
            .set_additional_needs("Cola") \
            .build()

        response = self.booking_api.create_booking(payload)
        assert response.status_code == 200
        booking_id = response.json()['bookingid']
        self.create_booking.append(booking_id)

        update_data = {
            "firstname": "Roor",
            "lastname": "Saaas",
        }

        response = self.booking_api.update_booking(booking_id, update_data, self.token)
        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json['firstname'] == 'Roor'
        assert resp_json['lastname'] == 'Saaas'
        print(f"Token used: {self.token}")
        print(f"Booking ID: {booking_id}")
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")


@pytest.mark.api
@pytest.mark.negative
@allure.feature('Booking API')
@allure.story('Негативные тест-кейсы')
class TestBookingNegative(BaseBookingTest):

    @allure.title('Создание бронирования с пустым телом запроса')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_booking_with_empty_payload(self):
        response = self.booking_api.create_booking({})
        assert response.status_code in [400, 500], f"Ожидался статус кода: {response.status_code}"



    @allure.title('Частичное обновление несуществующего бронирования')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_none_booking(self):
        update_data = {
            "firstname": "Test",
            "lastname": "User",
        }
        fake_id = 999999
        response = self.booking_api.update_booking(fake_id, update_data, self.token)

        assert response.status_code in [400, 405], f'Ожидался статус кода: {response.status_code}'

