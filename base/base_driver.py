from selenium.webdriver.common.action_chains import ActionChains


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def move_element_into_view(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()


