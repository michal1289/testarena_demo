from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.locators import TasksPageLocators
from common.operational_helpers import visibility_of_element_wait

class TasksPage:
    def __init__(self, driver):
        self.driver = driver

    def add_task(self, title, description, release, env, version, date):
        self.driver.find_element(By.XPATH, TasksPageLocators.add_task_button).click()
        self.driver.find_element(By.ID, TasksPageLocators.title).send_keys(title)
        self.driver.find_element(By.ID, TasksPageLocators.description).send_keys(description)
        self.driver.find_element(By.ID, TasksPageLocators.release).send_keys(release)
        self.driver.find_element(By.ID, TasksPageLocators.environments).send_keys(env)
        visibility_of_element_wait(self.driver, TasksPageLocators.environments_list)
        self.driver.find_element(By.ID, TasksPageLocators.environments).send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, TasksPageLocators.versions).send_keys(version)
        visibility_of_element_wait(self.driver, TasksPageLocators.versions_list)
        self.driver.find_element(By.ID, TasksPageLocators.versions).send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, TasksPageLocators.date).send_keys(date)
        self.driver.find_element(By.ID, TasksPageLocators.assign_to_me).click()
        self.driver.find_element(By.ID, TasksPageLocators.save_button).click()

    def get_add_task_message(self):
        visibility_of_element_wait(self.driver, TasksPageLocators.message_add_task)
        return self.driver.find_element(By.XPATH, TasksPageLocators.message_add_task).text
