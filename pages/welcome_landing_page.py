import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WelcomeLandingPage():

    def __init__(self, driver):
        self.driver = driver

    def click_on_register_link(self):
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
        register_link.click()
