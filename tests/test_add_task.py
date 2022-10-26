import pytest
import config_reader

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.TasksPage import TasksPage
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestAddTask(BaseTest):

    def test_add_task(self, setup):
        config = config_reader.load()
        self.driver.get(config['demo_url'])
        login_page = LoginPage(self.driver)
        login_page.login("administrator@testarena.pl", "sumXQQ72$L")
        main_page = MainPage(self.driver)
        main_page.open_tasks()
        task_add = TasksPage(self.driver)
        task_add.add_task("test title", "desc test", "test", "TEST", "V001", "2022-10-26 23:59")


