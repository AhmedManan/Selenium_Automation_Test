from base.base_test import BaseTest
from pages.cart_page import CartPage

class TestCart(BaseTest):

    def test_add_and_remove_item(self):
        cart_page = CartPage(self.driver)

        # Login
        self.login_page.open_login_page()
        self.login_page.login("standard_user", "secret_sauce")

        # Add item
        self.inventory_page.add_first_item_to_cart()
        self.inventory_page.open_cart()

        # Verify item in cart
        assert cart_page.is_item_in_cart(), "No item found in cart after adding."

        # Remove item
        cart_page.remove_item()
        assert not cart_page.is_item_in_cart(), "Item still in cart after removing."
