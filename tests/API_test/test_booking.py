import pytest
import allure
from API.booking_api import BookingAPI
from utils.payloader_builder import BookingPayloadBuilder

from schemas.booking_response_schema import booking_response_schema
from utils.schema_validator import SchemaValidator


@allure.feature('Booking API')

class TestBooking:

    @pytest.fixture(autouse=True)
    def setup(self, auth_token):
        self.booking_api = BookingAPI()
        self.token = auth_token
        self.create_booking = []


    @allure.story('Позитивный кейс: успешное создание бронирования')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_booking_positive(self):

        with allure.step('Создание тела запроса'):
            payload = BookingPayloadBuilder() \
                .set_firstname("SANYA") \
                .set_lastname("OJRA") \
                .set_totalprice(666) \
                .set_depositpaid(True) \
                .set_checkin("2025-04-01") \
                .set_checkout("2025-04-05") \
                .set_additional_needs("Espresso") \
                .build()

        with allure.step('Отправка запроса на создание брони'):
            response = self.booking_api.create_booking(payload)
            assert response.status_code == 200
            resp_json = response.json()
            booking_id = resp_json['bookingid']
            self.create_booking.append(booking_id)


        with allure.step('Проверка стркутуры ответа'):
            SchemaValidator.validate(resp_json, booking_response_schema)


    @allure.story('Негативный кейс: попытка бронирования без данных')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_booking_negative_miss_req_fds(self):
        with allure.step('Отправка пустого тела'):
            response = self.booking_api.create_booking({})
            assert response.status_code in [400, 500], f"Ожидался статус кода: {response.status_code}"


    @allure.story('Очистка: удаление созданного бронирования')
    def teardown(self):
        for booking_id in self.create_booking:
            with allure.step(f'Удаление бронирования с ID: {booking_id}'):
                response = self.booking_api.delete_booking(booking_id, self.token)
                assert response.status_code in [201, 204], f"Не удалось удалить бронирование {booking_id}"