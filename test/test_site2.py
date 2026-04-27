from pages.homepage import HomePage
from pages.product import ProductPage


def test_open(driver):
    homepage = HomePage(driver)
    homepage.open_site()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title('Samsung galaxy s6')
    # driver.get("https://www.demoblaze.com/")
    # galaxy = driver.find_element("xpath", "(//img[@class='card-img-top img-fluid'])[1]")
    # galaxy.click()
    # title = driver.find_element("xpath", "//h2[@class='name']")
    # assert title.text == 'Samsung galaxy s6'

def test_monitors(driver):
    driver.get("https://www.demoblaze.com/")
    monitors = driver.find_element("xpath", "(//a[@id='itemc'])[3]")
    monitors.click()
    bloks = driver.find_elements("xpath", "//div[@class='card-block']")
    count = len(bloks)
    assert count == 2