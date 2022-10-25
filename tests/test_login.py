import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.LoginPage import LoginPage
from pages.StartPage import StartPage


class TestLogin:
    @pytest.fixture
    def setup(self):
        url = "http://testarena.pl/demo"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_login_positive(self, setup):
        start_page = StartPage(self.driver)
        start_page.open_demo_page()
        login_page = LoginPage(self.driver)
        login_page.login("administrator@testarena.pl", "sumXQQ72$L")

    def test_login_negative(self, setup):
        start_page = StartPage(self.driver)
        start_page.open_demo_page()
        login_page = LoginPage(self.driver)
        login_page.login("demo_error@testarena.pl", "demo_error")
