from selenium.webdriver.common.by import By

from locators.locators import LoginPageLocators
from common.operational_helpers import visibility_of_element_wait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.ID, LoginPageLocators.email_input).send_keys(email)
        self.driver.find_element(By.ID, LoginPageLocators.password_input).send_keys(password)
        self.driver.find_element(By.ID, LoginPageLocators.login_button).click()

    def get_login_error(self):
        visibility_of_element_wait(self.driver, LoginPageLocators.login_error)
        return self.driver.find_element(By.XPATH, LoginPageLocators.login_error).text
