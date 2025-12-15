from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage


class TestLogin:

    def test_valid_login_and_logout(self, chrome):
        driver = chrome
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        # Open Login Page
        login_page.open_login_page()

        # Login
        login_page.login("standard_user", "secret_sauce")

        # Verify inventory
        assert inventory_page.is_inventory_displayed(), "Inventory not visible after login"

        # Logout
        # inventory_page.logout()

        # Verify redirection to login
        # assert "https://www.saucedemo.com/inventory.html" in driver.current_url

    def test_invalid_login(self, chrome):
        driver = chrome
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("wrong_user", "wrong_pass")
        error_message = login_page.get_error_message()
        assert "Username and password do not match" in error_message or "Epic sadface" in error_message
