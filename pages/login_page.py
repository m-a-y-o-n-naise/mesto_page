from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "auth-form__button")
    HEADER_USER = (By.CLASS_NAME, "header__user")

    def login(self, email, password):
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.find(self.PASSWORD_INPUT).send_keys(password)
        self.find(self.LOGIN_BUTTON).click()
        self.wait_for_element(self.HEADER_USER)
        return self