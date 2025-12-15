from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ProductPage:
    # -------------------------------------------------
    # page locators
    # -------------------------------------------------
    product_name = (By.CLASS_NAME, "name")
    add_to_cart  = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    # -------------------------------------------------
    # page actions
    # -------------------------------------------------

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 500

    def verify_product_name(self):
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(self.product_name)
        )

    def get_product_name(self) -> str:
        self.verify_product_name()
        return self.driver.find_element(*self.product_name).text