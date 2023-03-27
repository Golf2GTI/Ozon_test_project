from selenium.webdriver.common.by import By


# Локаторы для различных элементов на страницах
class BasePageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")

class CartPageLocators():
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "h1.bd2")
