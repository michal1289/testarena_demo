import pytest
import config_reader

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.TasksPage import TasksPage
from tests.base_test import BaseTest
from common.operational_helpers import random_string
from common.operational_helpers import date_time_now


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
        task_add.add_task("demo_" + random_string(5), random_string(20), random_string(8), "TEST", "V001",
                          date_time_now())
        assert task_add.get_add_task_message() == "Zadanie zostało dodane."
