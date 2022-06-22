from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CustomerCreatedPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def get_welcome_message(self, panel):
        if panel.lower() == 'left':
            message_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="leftPanel"]/p[@class="smallText"]')))

        elif panel.lower() == 'right':
            message_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="rightPanel"]')))

        return message_element.text

    def click_open_new_account_link(self):
        new_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Open New Account')))
        new_account_link.click()



