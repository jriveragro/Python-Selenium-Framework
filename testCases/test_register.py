import pytest
from pages.customer_created_page import CustomerLoginPage
from pages.register_page import RegisterPage
from pages.welcome_page import WelcomePage
import time


@pytest.mark.usefixtures('setup')
class TestRegister:
    def test_register(self):
        welcome_page = WelcomePage(self.driver, self.wait)
        register_page = RegisterPage(self.driver, self.wait)

        welcome_page.click_register_link()
        register_page.set_first_name('Archie')
        register_page.set_last_name('Wells')
        register_page.set_address('150 Testing Ave')
        register_page.set_city('Tampa')
        register_page.set_state('FL')
        register_page.set_zip_code('33607')
        register_page.set_phone_number('1001010001')
        register_page.set_ssn('100000001')
        register_page.set_user_name('awells')
        register_page.set_password('pwd#123')
        register_page.set_confirm_password('pwd#123')
        register_page.click_register_button()
        # assert welcome_page.get_page_title().endswith('parabank/register.htm')



