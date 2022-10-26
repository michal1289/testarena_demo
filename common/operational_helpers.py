import datetime
import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath was found

        :param driver: webdriver instance
        :param xpath: xpath of web element
        :param max_seconds_to_wait: maximum time in seconds to wait for element (default: 5)
        :param number_of_expected_elements: specifies minimum number of elements to be found
        :return: list of found elements
    """
    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements(By.XPATH, xpath)

        print(f'Total waiting {seconds}s')

        if len(elements) >= number_of_expected_elements:
            return elements

        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) >= number_of_expected_elements, \
                f'Expected {number_of_expected_elements} elements but found {len(elements)} for xpath {xpath} in time of {max_seconds_to_wait}s'

        time.sleep(1)


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
    return ''.join(random.choices(string.ascii_letters, k=size))


def date_time_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
