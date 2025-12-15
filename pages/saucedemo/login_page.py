from selenium.webdriver.common.by import By
from pages.saucedemo.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open_login_page(self):
        self.open_url("https://www.saucedemo.com/")

    def login(self, username, password):
        self.enter_text(self.driver.find_element(*self.USERNAME_INPUT), username)
        self.enter_text(self.driver.find_element(*self.PASSWORD_INPUT), password)
        self.click(self.driver.find_element(*self.LOGIN_BUTTON))

    def get_error_message(self):
        return self.get_text(self.driver.find_element(*self.ERROR_MESSAGE))
