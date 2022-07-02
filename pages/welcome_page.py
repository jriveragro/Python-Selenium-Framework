from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.register_page import RegisterPage
from pages.accounts_overview import AccountsOverviewPage


class WelcomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # =====================================================================================
    # Locators ----------------------------------------------------------------------------
    # =====================================================================================
    USER_NAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "input[type='submit'][value='Log In']"
    REGISTER_LINK_TEXT = "Register"

    # =====================================================================================
    # Element-wrapper methods -------------------------------------------------------------
    # =====================================================================================
    def get_user_name_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.USER_NAME_INPUT)

    def get_password_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.PASSWORD_INPUT)

    def get_login_button(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.LOGIN_BUTTON)

    def get_register_link(self):
        return self.wait_for_element_to_be_clickable(By.LINK_TEXT, self.REGISTER_LINK_TEXT)

    # =====================================================================================
    # Actions -----------------------------------------------------------------------------
    # =====================================================================================
    def set_user_name(self, user_name):
        self.get_user_name_field().clear()
        self.get_user_name_field().send_keys(user_name)

    def set_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def click_register_link(self):
        self.get_register_link().click()
        register_page = RegisterPage(self.driver)
        return register_page

    def log_in_existing_user(self, username, password):
        self.set_user_name(username)
        self.set_password(password)
        self.click_login_button()
        account_overview_page = AccountsOverviewPage(self.driver)
        return account_overview_page





    

