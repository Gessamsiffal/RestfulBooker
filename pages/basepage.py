from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://automationintesting.online'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find_elem(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all_elem(self, locator: tuple):
        return self.driver.find_elements(*locator)
