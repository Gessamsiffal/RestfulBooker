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
        logger.debug(f'Вводим логин: {login} и пароль: {password}')
        email_field = self.find_elem(loc.FIELD_LOGIN_LOC).send_keys(login)
        password_field = self.find_elem(loc.FIELD_PASSWORD_LOC).send_keys(password)
        btn_sign = self.find_elem(loc.BTN_LOGIN_LOC).click()
        
    
    def correct_login(self):
        row_correct = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.TEXT_TRUE_LOGIN)
        )
        return row_correct
    
    
    def incorrect_login(self):
        row_incorrect = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.TEXT_FALSE_LOGIN)
        )
        return row_incorrect
