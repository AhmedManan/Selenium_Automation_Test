from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.inventory_page import InventoryPage

class TestCart:

    def test_add_and_remove_item(self, chrome):
        driver = chrome
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # Login
        login_page.open_login_page()
        login_page.login("standard_user", "secret_sauce")

        # Add item
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        # Verify item in cart
        assert cart_page.is_item_in_cart(), "No item found in cart after adding."

        # Remove item
        cart_page.remove_item()
        assert not cart_page.is_item_in_cart(), "Item still in cart after removing."
