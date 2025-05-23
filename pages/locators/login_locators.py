from selenium.webdriver.common.by import By

#Локаторы логина, пароля, кнопки входа
FIELD_LOGIN_LOC = (By.ID, 'username')
FIELD_PASSWORD_LOC = (By.ID, 'password')
BTN_LOGIN_LOC = (By.ID, 'doLogin')
BTN_LOGOUT_LOC = (By.XPATH, "//button[text()='Logout']")
PAGE_URL = '/admin'

#Локаторы сценариев
TEXT_TRUE_LOGIN = (By.XPATH, '//div[contains(@class, "rowHeader")]//p[text()="Room #"]')
TEXT_FALSE_LOGIN = (By.CSS_SELECTOR, 'div.alert.alert-danger')