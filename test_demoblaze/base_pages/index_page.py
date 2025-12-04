from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class IndexPage:
    login_popup_xpath="//*[@id='login2']"
    textbox_username_id= "loginusername"
    textbox_password_id= "loginpassword"
    button_login_xpath= "//button[text()='Log in']"
    logged_in_user_xpath = '//*[@id="nameofuser"]'

    # -------------------------------------------------
    # page actions
    # -------------------------------------------------

    def __init__(self, driver):
        self.driver = driver
    def get_login_popup(self):
        self.driver.find_element(By.XPATH, self.login_popup_xpath).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, self.textbox_username_id))
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, self.textbox_password_id))
        ).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def get_logged_in_user(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.logged_in_user_xpath))
        ).text