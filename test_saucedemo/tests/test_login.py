from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_logout_valid_user(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Step 1: Open login page
    login_page.open_login_page()

    # Step 2: Perform login
    login_page.login("standard_user", "secret_sauce")

    # Step 3: Verify inventory page
    assert inventory_page.is_inventory_displayed(), "Inventory page not displayed after login!"

    # Step 4: Logout
    inventory_page.logout()

    # Step 5: Verify back on login page
    assert "saucedemo.com" in driver.current_url
