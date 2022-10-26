from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from locators.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def select_project(self):
        drop = Select(self.driver.find_element(By.ID, MainPageLocators.project_list))
        drop.select_by_visible_text("PROJEKT_DK")

    def open_tasks(self):
        self.driver.find_element(By.LINK_TEXT, MainPageLocators.menu_tasks).click()

