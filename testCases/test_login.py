import pytest
from pages.welcome_page import WelcomePage
from utilities.utils import Utils


@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_successful_login(self):
        wp = WelcomePage(self.driver)
        account_overview_page = wp.log_in_existing_user("eramberxiomara357", "hola@741")
        ut = Utils()
        ut.assert_page_url_ends_with(account_overview_page.get_page_url(), "/parabank/overview.htm")
