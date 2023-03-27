import pytest
from selenium import webdriver


# Фикстура, которая инициализирует браузер и закрывает его после выполнения теста.
@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
