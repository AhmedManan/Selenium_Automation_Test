from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def is_inventory_displayed(self):
        return self.is_element_displayed(self.driver.find_element(*self.INVENTORY_CONTAINER))

    def logout(self):
        self.click(self.driver.find_element(*self.BURGER_MENU))
        self.click(self.driver.find_element(*self.LOGOUT_LINK))
