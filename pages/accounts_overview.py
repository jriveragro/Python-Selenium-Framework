from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class AccountsOverviewPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # =====================================================================================
    # Locators ----------------------------------------------------------------------------
    # =====================================================================================
    WELCOME_MESSAGE_LEFT_PANEL = "//div[@id='leftPanel']/p[@class='smallText']"
    WELCOME_MESSAGE_RIGHT_PANEL = "//div[@class='ng-scope']/h1[@class='title']"

    # =====================================================================================
    # Element-wrapper methods -------------------------------------------------------------
    # =====================================================================================
    def get_welcome_message_left_panel_text(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.WELCOME_MESSAGE_LEFT_PANEL)

    def get_welcome_message_right_panel_text(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.WELCOME_MESSAGE_RIGHT_PANEL)

    # =====================================================================================
    # Actions -----------------------------------------------------------------------------
    # =====================================================================================
    def get_welcome_message(self, panel):
        if panel.lower() == 'left':
            return self.get_welcome_message_left_panel_text().text

        elif panel.lower() == 'right':
            return self.get_welcome_message_right_panel_text().text
