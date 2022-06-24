from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CustomerCreatedPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_welcome_message(self, panel):
        if panel.lower() == 'left':
            message_element = self.wait_for_visibility_of_element(By.XPATH, '//div[@id="leftPanel"]/p[@class="smallText"]')

        elif panel.lower() == 'right':
            message_element = self.wait_for_visibility_of_element(By.CSS_SELECTOR, 'div[id="rightPanel"]')

        return message_element.text

    def click_open_new_account_link(self):
        new_account_link = self.wait_for_element_to_be_clickable(By.LINK_TEXT, 'Open New Account')
        new_account_link.click()



