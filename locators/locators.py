class StartPageLocators:
    demo_button = "//a[@href='http://demo.testarena.pl/']"


class LoginPageLocators:
    email_input = "email"
    password_input = "password"
    login_button = "login"
    login_error = "//div[@class='login_form_error']"


class MainPageLocators:
    project_list = "activeProject"
    menu_tasks = "Zadania"


class TasksPageLocators:
    add_task_button = "//a[contains(text(),'Dodaj zadanie')]"
    title = "title"
    description = "description"
    release = "releaseName"
    environments = "token-input-environments"
    environments_list = "//li[@class='token-input-dropdown-item2-facebook token-input-selected-dropdown-item-facebook']"
    versions = "token-input-versions"
    versions_list = "//li[@class='token-input-dropdown-item2-facebook token-input-selected-dropdown-item-facebook']"
    date = "dueDate"
    assign_to_me = "j_assignToMe"
    save_button = "save"
    message_add_task = "//div[@id='j_info_box']//p"
