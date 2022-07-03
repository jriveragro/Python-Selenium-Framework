import pytest
from pages.welcome_page import WelcomePage
from utilities.utils import Utils


@pytest.mark.usefixtures('setup')
class TestRegister:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.wp = WelcomePage(self.driver)
        self.ut = Utils()

    def test_register(self):
        register_page = self.wp.click_register_link()
        customer_created_page = register_page.register_new_user("Eramber", "Xiomara", "50480 Amber Dr", "Miami", "FL", "33022", "2003001001", "100101001", "eramberxiomara357", "hola@741")
        self.ut.assert_page_url_ends_with(customer_created_page.get_page_url(), "/parabank/register.htm")
