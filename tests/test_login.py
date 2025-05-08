import pytest
import os
from pages.login_page import CustomerLogin
from dotenv import load_dotenv


load_dotenv()


@pytest.mark.parametrize('login, password', [
    (os.getenv('USER_LOGIN_1'), os.getenv('USER_PASSWORD_1')),
    (os.getenv('USER_LOGIN_2'), os.getenv('USER_PASSWORD_2')),
])
def test_login_page(login_page, login, password):
    login_page.open_page()
    login_page.fill_form(login, password)
