from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class AccountsOverviewPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_welcome_message(self, panel):
        if panel.lower() == 'left':
            message_element = self.wait_for_visibility_of_element(By.XPATH, '//div[@id="leftPanel"]/p[@class="smallText"]')

        elif panel.lower() == 'right':
            message_element = self.wait_for_visibility_of_element(By.XPATH, '//div[@class="ng-scope"]/h1[@class="title"]')

        return message_element.text



