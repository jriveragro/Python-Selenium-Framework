import pytest
import re
from pages.welcome_page import WelcomePage
from pages.accounts_overview import AccountsOverviewPage


@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login(self):
        welcome_page = WelcomePage(self.driver)

        welcome_page.log_in_existing_user("cdeale", "pwd#123")

        assert re.match(".+\/parabank\/login\.htm.+", welcome_page.get_page_url())

