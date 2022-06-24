import pytest
from pages.register_page import RegisterPage
from pages.welcome_page import WelcomePage
from pages.customer_created_page import CustomerCreatedPage


@pytest.mark.usefixtures('setup')
class TestRegister:
    def test_register(self):
        welcome_page = WelcomePage(self.driver)
        register_page = RegisterPage(self.driver)
        customer_created_page = CustomerCreatedPage(self.driver)

        welcome_page.click_register_link()
        register_page.set_first_name('bando')
        register_page.set_last_name('tef')
        register_page.set_address('155 Black Box Ln')
        register_page.set_city('Tampa')
        register_page.set_state('FL')
        register_page.set_zip_code('33607')
        register_page.set_phone_number('1001010001')
        register_page.set_ssn('100000001')
        register_page.set_user_name('btef')
        register_page.set_password('pwd#123')
        register_page.set_confirm_password('pwd#123')
        register_page.click_register_button()
        # assert welcome_page.get_page_title().endswith('parabank/register.htm')

        print(f'This is the message in the left panel:> {customer_created_page.get_welcome_message("left")}')
        print(f'This is the message in the right panel:> {customer_created_page.get_welcome_message("right")}')
