from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class RegisterPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_first_name(self, first_name):
        first_name_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.firstName')
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def set_last_name(self, last_name):
        last_name_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.lastName')
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def set_address(self, address):
        address_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.address.street')
        address_input.clear()
        address_input.send_keys(address)

    def set_city(self, city):
        city_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.address.city')
        city_input.clear()
        city_input.send_keys(city)

    def set_state(self, state):
        state_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.address.state')
        state_input.clear()
        state_input.send_keys(state)

    def set_zip_code(self, zip_code):
        zip_code_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.address.zipCode')
        zip_code_input.clear()
        zip_code_input.send_keys(zip_code)

    def set_phone_number(self, phone_number):
        phone_number_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.phoneNumber')
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def set_ssn(self, ssn):
        ssn_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.ssn')
        ssn_input.clear()
        ssn_input.send_keys(ssn)

    def set_user_name(self, user_name):
        user_name_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.username')
        user_name_input.clear()
        user_name_input.send_keys(user_name)

    def set_password(self, password):
        password_input = self.wait_for_element_to_be_clickable(By.ID, 'customer.password')
        password_input.clear()
        password_input.send_keys(password)

    def set_confirm_password(self, confirm_password):
        confirm_password_input = self.wait_for_element_to_be_clickable(By.ID, 'repeatedPassword')
        confirm_password_input.clear()
        confirm_password_input.send_keys(confirm_password)

    def click_register_button(self):
        register_link = self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[type="submit"][value="Register"]')
        register_link.click()
