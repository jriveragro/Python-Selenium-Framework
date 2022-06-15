from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_first_name(self, first_name):
        first_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.firstName')))
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.lastName')))
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def enter_address(self, address):
        address_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.address.street')))
        address_input.clear()
        address_input.send_keys(address)

    def enter_city(self, city):
        city_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.address.city')))
        city_input.clear()
        city_input.send_keys(city)

    def enter_state(self, state):
        state_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.address.state')))
        state_input.clear()
        state_input.send_keys(state)

    def enter_zip_code(self, zip_code):
        zip_code_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.address.zipCode')))
        zip_code_input.clear()
        zip_code_input.send_keys(zip_code)

    def enter_phone_number(self, phone_number):
        phone_number_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.phoneNumber')))
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def enter_ssn(self, ssn):
        ssn_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.ssn')))
        ssn_input.clear()
        ssn_input.send_keys(ssn)

    def enter_user_name(self, user_name):
        user_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.username')))
        user_name_input.clear()
        user_name_input.send_keys(user_name)

    def enter_password(self, password):
        password_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'customer.password')))
        password_input.clear()
        password_input.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'repeatedPassword')))
        confirm_password_input.clear()
        confirm_password_input.send_keys(confirm_password)

    def click_on_register_button(self):
        register_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]')))
        register_link.click()
