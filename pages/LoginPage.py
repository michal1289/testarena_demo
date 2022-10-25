from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = "email"
        self.password_input = "password"
        self.login_button = "login"

    def login(self, email, password):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.ID, self.email_input).send_keys(email)
        self.driver.find_element(By.ID, self.password_input).send_keys(password)
        self.driver.find_element(By.ID, self.login_button).click()
