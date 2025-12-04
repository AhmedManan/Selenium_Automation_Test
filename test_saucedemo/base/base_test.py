import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("setup_driver")
class BaseTest:
    def setup_method(self):
        # Initialize reusable page objects
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
