class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def open_site(self):
        self.driver.get('https://www.demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy = self.driver.find_element("xpath", "(//img[@class='card-img-top img-fluid'])[1]")
        galaxy.click()


