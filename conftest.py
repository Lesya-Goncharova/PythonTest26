from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window() # окно на весь экран
    driver.implicitly_wait(3) # неявное ожидание появления элементов на странице
    yield driver
    driver.close()