from pages.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def go_to_cart(self):
        button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        button.click()

