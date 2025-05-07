from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import pytest



@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture()
def login_page(driver):
    return

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()