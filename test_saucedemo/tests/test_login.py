from base.base_test import BaseTest

class TestLogin(BaseTest):

    def test_valid_login_and_logout(self):
        # Open Login Page
        self.login_page.open_login_page()

        # Login
        self.login_page.login("standard_user", "secret_sauce")

        # Verify inventory
        assert self.inventory_page.is_inventory_displayed(), "Inventory not visible after login"

        # Logout
        self.inventory_page.logout()

        # Verify redirection to login
        assert "saucedemo.com" in self.driver.current_url

    def test_invalid_login(self):
        self.login_page.open_login_page()
        self.login_page.login("wrong_user", "wrong_pass")
        error_message = self.login_page.get_error_message()
        assert "Username and password do not match" in error_message or "Epic sadface" in error_message
