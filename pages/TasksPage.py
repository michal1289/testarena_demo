from selenium.webdriver.common.by import By

from locators.locators import TasksPageLocators


class TasksPage:
    def __init__(self, driver):
        self.driver = driver

    def add_task(self, title, description, release, env, version, date):
        self.driver.find_element(By.XPATH, TasksPageLocators.add_task_button).click()
        self.driver.find_element(By.ID, TasksPageLocators.title).send_keys(title)
        self.driver.find_element(By.ID, TasksPageLocators.description).send_keys(description)
        self.driver.find_element(By.ID, TasksPageLocators.release).send_keys(release)
        self.driver.find_element(By.ID, TasksPageLocators.environments).send_keys(env)
        self.driver.find_element(By.ID, TasksPageLocators.versions).send_keys(version)
        self.driver.find_element(By.ID, TasksPageLocators.date).send_keys(date)
        self.driver.find_element(By.ID, TasksPageLocators.assign_to_me).click()
        self.driver.find_element(By.ID, TasksPageLocators.save_button).click()

