from selenium.webdriver.common.by import By

from locators.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_tasks(self):
        self.driver.find_element(By.LINK_TEXT, MainPageLocators.menu_tasks).click()

