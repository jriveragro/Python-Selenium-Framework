import pytest
from pages.welcome_page import WelcomePage
from pages.accounts_overview import AccountsOverviewPage


@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login(self):
        welcome_page = WelcomePage(self.driver)
        accounts_overview = AccountsOverviewPage(self.driver)

        welcome_page.set_user_name('btef')
        welcome_page.set_password('pwd#123')
        welcome_page.click_login_button()
        # assert welcome_page.get_page_title().endswith('parabank/register.htm')

        print(f'This is the message in the left panel:> {accounts_overview.get_welcome_message("left")}')
        print(f'This is the message in the right panel:> {accounts_overview.get_welcome_message("right")}')

