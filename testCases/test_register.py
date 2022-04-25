import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.welcome_landing_page import WelcomeLandingPage
from pages.register_page import RegisterPage


@pytest.mark.usefixtures('setup')
class TestRegister():
    def test_register(self):
        welcome_page = WelcomeLandingPage(self.driver)
        register_page = RegisterPage(self.driver)

        welcome_page.click_on_register_link()

        register_page.enter_first_name('Archie')
        register_page.enter_last_name('Wells')
        register_page.enter_address('Wells')
        register_page.enter_city('Wells')
        register_page.enter_state('Wells')
        register_page.enter_zip_code('Wells')
        register_page.enter_phone_number('Wells')
        register_page.enter_ssn('Wells')
        register_page.enter_user_name('Wells')
        register_page.enter_password('Wells')
        register_page.enter_confirm_password('Wells')





register = TestRegister()
register.test_register()
