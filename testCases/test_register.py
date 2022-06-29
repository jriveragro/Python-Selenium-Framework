import pytest
import re
from pages.register_page import RegisterPage
from pages.welcome_page import WelcomePage
from pages.customer_created_page import CustomerCreatedPage


@pytest.mark.usefixtures('setup')
class TestRegister:
    def test_register(self):
        welcome_page = WelcomePage(self.driver)
        register_page = RegisterPage(self.driver)

        welcome_page.click_register_link()
        register_page.register_new_user("Cona", "Deale",
                                        "545 Amber St", "Orlando", "FL", "33022", "2003001001",
                                        "100101001", "cdeale", "pwd#123")

        assert re.match(".+\/parabank\/register\.htm", welcome_page.get_page_url())
