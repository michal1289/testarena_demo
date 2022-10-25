class TasksPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_task_button = "//a[contains(text(),'Dodaj zadanie')]"
        self.title = "title"
        self.description = "description"
        self.release = "releaseName"
        self.environments = "token-input-environments"
        self.versions = "token-input-versions"
        self.date = "dueDate"
        self.assign_to_me = "j_assignToMe"
        self.save_button = "save"
        self.message_add_task = "//div[@id='j_info_box']//p"
