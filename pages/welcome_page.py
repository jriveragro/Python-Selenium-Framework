from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class WelcomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_user_name(self, user_name):
        user_name_input = self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[name="username"]')
        user_name_input.clear()
        user_name_input.send_keys(user_name)

    def set_password(self, password):
        password_input = self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[type="submit"][value="Log In"]')
        login_button.click()

    def click_register_link(self):
        register_link = self.wait_for_element_to_be_clickable(By.LINK_TEXT, 'Register')
        register_link.click()



    

