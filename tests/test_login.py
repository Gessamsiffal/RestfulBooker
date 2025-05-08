import pytest
import os
import allure
from dotenv import load_dotenv


load_dotenv()

@allure.feature("Авторизация")
@allure.story("Правильный логин")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.positive
@pytest.mark.parametrize('login, password', [
    (os.getenv('USER_LOGIN_1'), os.getenv('USER_PASSWORD_1'))
])
def test_correct_login_page(login_page, login, password):
    login_page.open_page()
    login_page.fill_form(login, password)
    login_page.correct_login('Room #')

@allure.feature("Авторизация")
@allure.story("Неправильные данные")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize('login, password', [
    (os.getenv('USER_LOGIN_2'), os.getenv('USER_PASSWORD_2'))
])
def test_incorrect_login_page(login_page, login, password):
    login_page.open_page()
    login_page.fill_form(login, password)
    login_page.incorrect_login('Invalid credentials')

