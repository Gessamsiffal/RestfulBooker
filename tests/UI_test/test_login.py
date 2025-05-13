import pytest
import os
import allure
from dotenv import load_dotenv


load_dotenv()

@allure.feature("Авторизация")
@pytest.mark.login
class TestLogin:

    @allure.story("Правильный логин")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.parametrize('login, password', [
        (os.getenv('USER_LOGIN_1'), os.getenv('USER_PASSWORD_1'))
    ])
    def test_correct_login_page(self, login_page, login, password):
        with allure.step('Открываем страницу'):
            login_page.open_page()
        with allure.step('Заполняем логин и пароль'):
            login_page.fill_form(login, password)
        with allure.step('Делаем проверку'):
            correct_elem = login_page.correct_login()
            assert correct_elem.text == 'Room #', f'Ожидали "Room #", но получили "{correct_elem.text}"'

    @allure.story("Неправильные данные")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    @pytest.mark.parametrize('login, password', [
        (os.getenv('USER_LOGIN_2'), os.getenv('USER_PASSWORD_2'))
    ])
    def test_incorrect_login_page(self, login_page, login, password):
        with allure.step('Открываем страницу'):
            login_page.open_page()
        with allure.step('Заполняем логин и пароль'):
            login_page.fill_form(login, password)
        with allure.step('Делаем проверку'):
            incorrect_elem = login_page.incorrect_login()
            assert incorrect_elem.text == 'Invalid credentials', f'Ожидали "Invalid credentials", но получили "{incorrect_elem.text}"'
