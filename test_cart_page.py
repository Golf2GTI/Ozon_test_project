from pages.cart_page import CartPage

link = "https://www.ozon.ru/cart"

def test_guest_cart_should_be_empty(browser):
    page = CartPage(browser, link)
    page.open()
    page.is_cart_empty()
