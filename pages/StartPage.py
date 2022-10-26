from selenium.webdriver.common.by import By

from locators.locators import StartPageLocators


class StartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_demo_page(self):
        self.driver.find_element(By.XPATH, StartPageLocators.demo_button).click()


