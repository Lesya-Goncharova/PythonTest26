def test_open(driver):
    driver.get("https://www.demoblaze.com/")
    galaxy = driver.find_element("xpath", "(//img[@class='card-img-top img-fluid'])[1]")
    galaxy.click()
    title = driver.find_element("xpath", "//h2[@class='name']")
    assert title.text == 'Samsung galaxy s6'

def test_monitors(driver):
    driver.get("https://www.demoblaze.com/")
    monitors = driver.find_element("xpath", "(//a[@id='itemc'])[3]")
    monitors.click()
    bloks = driver.find_elements("xpath", "//div[@class='card-block']")
    count = len(bloks)
    assert count == 2