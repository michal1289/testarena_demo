from selenium.webdriver.common.by import By


class StartPage:
    def __init__(self, driver):
        self.driver = driver
        self.demo_button = "//a[@href='http://demo.testarena.pl/']"

    def open_demo_page(self):
        self.driver.find_element(By.XPATH, self.demo_button).click()


