
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.administration_button = "//div[@class='header_admin']"
        self.project_dropdown = "activeProject_chosen"
        self.project_chosen_search = "//div[@class='chosen-search']//input"
        self.project_chosen = "//li[contains(text(),'%s')]"
        self.menu_tasks = "//a[@href='http://demo.testarena.pl/PP1/tasks']"
