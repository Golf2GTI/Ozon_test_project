from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def is_cart_empty(self):
        self.is_element_present(*CartPageLocators.CART_EMPTY_MESSAGE)
