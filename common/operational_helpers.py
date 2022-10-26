import datetime
import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def visibility_of_element_wait(driver, xpath, timeout=10) -> WebElement:
    """Checking if element specified by xpath is visible on page
        :param driver: webdriver or event firing webdriver instance
        :param xpath: xpath of web element
        :param timeout: time after looking for element will be stopped (default: 10)
        :return: first element in list of found elements
    """
    timeout_message = f"Element for xpath: '{xpath}' and url: {driver.current_url} not found in {timeout} seconds"
    locator = (By.XPATH, xpath)
    element_located = EC.visibility_of_element_located(locator)
    if hasattr(driver, 'wrapped_driver'):
        unwrapped_driver = driver.wrapped_driver
        wait = WebDriverWait(unwrapped_driver, timeout)
    else:
        wait = WebDriverWait(driver, timeout)
    return wait.until(element_located, timeout_message)


def random_string(size):
    """ Random text to type
    :param size: text size
    :return:text with the selected size
    """
    return ''.join(random.choices(string.ascii_letters, k=size))


def date_time_now():
    """Data and time now
    :return:data and time now
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
