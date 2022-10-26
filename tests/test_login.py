import pytest
import config_reader

from pages.LoginPage import LoginPage
from pages.StartPage import StartPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    def test_login_positive(self, setup):
        config = config_reader.load()
        self.driver.get(config['base_url'])
        start_page = StartPage(self.driver)
        start_page.open_demo_page()
        login_page = LoginPage(self.driver)
        login_page.login(config['correct_user'], config['correct_user_pass'])
        assert self.driver.title == "Kokpit - TestArena Demo"

    def test_login_negative(self, setup):
        config = config_reader.load()
        self.driver.get(config['base_url'])
        start_page = StartPage(self.driver)
        start_page.open_demo_page()
        login_page = LoginPage(self.driver)
        login_page.login(config['incorrect_user'], config['incorrect_user_pass'])
        assert login_page.get_login_error() == "Adres e-mail i/lub hasło są niepoprawne."
