import pytest
from pages.welcome_page import WelcomePage
from utilities.utils import Utils


@pytest.mark.usefixtures('setup')
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.wp = WelcomePage(self.driver)
        self.ut = Utils()

    def test_successful_login(self):
        account_overview_page = self.wp.log_in_existing_user("eramberxiomara357", "hola@741")
        self.ut.assert_page_url_ends_with(account_overview_page.get_page_url(), "/parabank/overview.htm")
