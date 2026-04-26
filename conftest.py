from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3) #неявное ожидание появления элементов на странице
    yield browser
    browser.close()