from pages.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


# Создаём класс базовой страницы от которой будут наследоваться все последующие
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Функция открытия браузером ссылки
    def open(self):
        self.browser.get(self.url)

    # Функция, которая проверяет, есть ли элемент на странице, если его нет - ошибка NoSuchElementException.
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True

    # Функция перехода в корзину
    def go_to_cart(self):
        button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        button.click()
