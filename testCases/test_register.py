import pytest
from pages.customer_login_page import CustomerLoginPage
from pages.register_page import RegisterPage
import time


@pytest.mark.usefixtures('setup')
class TestRegister:
    def test_register(self):
        customer_login_page = CustomerLoginPage(self.driver, self.wait)
        register_page = RegisterPage(self.driver, self.wait)

        customer_login_page.click_on_register_link()

        register_page.enter_first_name('Archie')
        register_page.enter_last_name('Wells')
        register_page.enter_address('150 Testing Ave')
        register_page.enter_city('Tampa')
        register_page.enter_state('FL')
        register_page.enter_zip_code('33607')
        register_page.enter_phone_number('1001010001')
        register_page.enter_ssn('100000001')
        register_page.enter_user_name('awells')
        register_page.enter_password('pwd#123')
        register_page.enter_confirm_password('pwd#123')
        register_page.click_on_register_button()

        time.sleep(15)
