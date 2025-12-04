from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_item_in_cart(self):
        return len(self.driver.find_elements(*self.CART_ITEM)) > 0

    def remove_item(self):
        self.click(self.driver.find_element(*self.REMOVE_BUTTON))

    def proceed_to_checkout(self):
        self.click(self.driver.find_element(*self.CHECKOUT_BUTTON))
