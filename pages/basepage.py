from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    BASE_URL = 'https://automationintesting.online'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find_elem(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all_elem(self, locator: tuple):
        return self.driver.find_elements(*locator)
