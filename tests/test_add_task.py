import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestAddTask:
    @pytest.fixture
    def setup(self):
        url = "http://testarena.pl/demo"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_add_task(self, setup):
        pass
