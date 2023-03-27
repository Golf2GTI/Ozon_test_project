from pages.base_page import BasePage

link = "https://www.ozon.ru/my/main"


def test_go_to_cart(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_cart()
