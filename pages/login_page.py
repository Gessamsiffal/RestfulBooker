import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import get_logger
from pages.basepage import BasePage
from pages.locators import login_locators as loc

logger = get_logger('LOGIN')

class CustomerLogin(BasePage):

    PAGE_URL = loc.PAGE_URL

    def fill_form(self, login, password):
        with allure.step('Вводим логин и пароль на странице админ панели'):
            logger.debug(f'Вводим логин: {login} и пароль: {password}')
            email_field = self.find_elem(loc.FIELD_LOGIN_LOC).send_keys(login)
            password_field = self.find_elem(loc.FIELD_PASSWORD_LOC).send_keys(password)
            btn_sign = self.find_elem(loc.BTN_LOGIN_LOC).click()
        
    
    def correct_login(self, text):
        with allure.step('Проверка корректности входа'):
            row_correct = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(loc.TEXT_TRUE_LOGIN)
            )
            assert row_correct.text == text
    
    
    def incorrect_login(self, text):
        with allure.step('Проверка неправильного входа'):
            row_incorrect = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(loc.TEXT_FALSE_LOGIN)
            )
            assert row_incorrect.text == text
