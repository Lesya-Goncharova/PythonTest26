class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title(self, title):
        page_title = self.driver.find_element("xpath", "//h2[@class='name']")
        assert page_title.text == title