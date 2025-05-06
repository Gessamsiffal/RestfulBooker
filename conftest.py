from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest



@pytest.fixture()
def driver():
    options = Options('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()