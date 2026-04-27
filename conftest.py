from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window() # окно на весь экран
    browser.implicitly_wait(3) # неявное ожидание появления элементов на странице
    yield browser
    browser.close()