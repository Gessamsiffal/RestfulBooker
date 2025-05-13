from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import pytest
from time import sleep

from API.booking_api import BookingAPI
from pages.login_page import CustomerLogin
from API.auth_api import AuthApi


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)

    yield chrome_driver

    sleep(5)
    chrome_driver.close()


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture()
def booking_api():
    return BookingAPI()

@pytest.fixture(scope="module")
def auth_token():
    auth_api = AuthApi()
    response = auth_api.create_token()
    assert response.status_code == 200
    return response.json()["token"]