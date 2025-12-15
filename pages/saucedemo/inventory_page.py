from selenium.webdriver.common.by import By
from pages.saucedemo.base_page import BasePage

class InventoryPage(BasePage):
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def is_inventory_displayed(self):
        return self.is_element_displayed(self.driver.find_element(*self.INVENTORY_CONTAINER))

    def add_first_item_to_cart(self):
        first_item_add_btn = self.driver.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        self.click(first_item_add_btn)

    def open_cart(self):
        self.click(self.driver.find_element(*self.CART_ICON))

    def logout(self):
        self.click(self.driver.find_element(*self.BURGER_MENU))
        self.click(self.driver.find_element(*self.LOGOUT_LINK))
