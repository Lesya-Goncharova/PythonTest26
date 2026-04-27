class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def open_site(self):
        self.driver.get('https://www.demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy = self.driver.find_element("xpath", "(//img[@class='card-img-top img-fluid'])[1]")
        galaxy.click()

    def click_monitors(self):
        monitors = self.driver.find_element("xpath", "(//a[@id='itemc'])[3]")
        monitors.click()

    def check_products_count(self, count):
        bloks = self.driver.find_elements("xpath", "//div[@class='card-block']")
        assert len(bloks) == count


