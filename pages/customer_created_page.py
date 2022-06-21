from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CustomerCreatedPage(BaseDriver):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_welcome_message_left_panel(self):
        message_element = self.wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'div[id="leftPanel"]'))
        return message_element.text

    def get_welcome_message_right_panel(self):
        message_element = self.wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'div[id="rightPanel"]'))
        return message_element.text

    def click_open_new_account_link(self):
        new_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Open New Account')))
        new_account_link.click()



