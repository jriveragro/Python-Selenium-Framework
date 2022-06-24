from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def get_page_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def move_element_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_visibility_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element



