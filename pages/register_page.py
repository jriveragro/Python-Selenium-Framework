from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class RegisterPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # =====================================================================================
    # Locators ----------------------------------------------------------------------------
    # =====================================================================================
    FIRST_NAME_INPUT = "input[id='customer.firstName']"
    LAST_NAME_INPUT = "input[id='customer.lastName']"
    ADDRESS_INPUT = "input[id='customer.address.street']"
    CITY_INPUT = "input[id='customer.address.city']"
    STATE_INPUT = "input[id='customer.address.state']"
    ZIP_CODE_INPUT = "input[id='customer.address.zipCode']"
    PHONE_NUMBER_INPUT = "input[id='customer.phoneNumber']"
    SSN_INPUT = "input[id='customer.ssn']"
    USER_NAME_INPUT = "input[id='customer.username']"
    PASSWORD_INPUT = "input[id='customer.password']"
    CONFIRM_PASSWORD_INPUT = "input[id='repeatedPassword']"
    REGISTER_BUTTON = "input[type='submit'][value='Register']"

    # =====================================================================================
    # Element-wrapper methods -------------------------------------------------------------
    # =====================================================================================
    def get_first_name_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.FIRST_NAME_INPUT)

    def get_last_name_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.LAST_NAME_INPUT)

    def get_address_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.ADDRESS_INPUT)

    def get_city_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.CITY_INPUT)

    def get_state_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.STATE_INPUT)

    def get_zipcode_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.ZIP_CODE_INPUT)

    def get_phone_number_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.PHONE_NUMBER_INPUT)

    def get_ssn_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.SSN_INPUT)

    def get_user_name_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.USER_NAME_INPUT)

    def get_password_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.PASSWORD_INPUT)

    def get_confirm_password_field(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.CONFIRM_PASSWORD_INPUT)

    def get_register_button(self):
        return self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, self.REGISTER_BUTTON)

    # =====================================================================================
    # Actions -----------------------------------------------------------------------------
    # =====================================================================================
    def set_first_name(self, first_name):
        self.get_first_name_field().clear()
        self.get_first_name_field().send_keys(first_name)

    def set_last_name(self, last_name):
        self.get_last_name_field().clear()
        self.get_last_name_field().send_keys(last_name)

    def set_address(self, address):
        self.get_address_field().clear()
        self.get_address_field().send_keys(address)

    def set_city(self, city):
        self.get_city_field().clear()
        self.get_city_field().send_keys(city)

    def set_state(self, state):
        self.get_state_field().clear()
        self.get_state_field().send_keys(state)

    def set_zip_code(self, zip_code):
        self.get_zipcode_field().clear()
        self.get_zipcode_field().send_keys(zip_code)

    def set_phone_number(self, phone_number):
        self.get_phone_number_field().clear()
        self.get_phone_number_field().send_keys(phone_number)

    def set_ssn(self, ssn):
        self.get_ssn_field().clear()
        self.get_ssn_field().send_keys(ssn)

    def set_user_name(self, user_name):
        self.get_user_name_field().clear()
        self.get_user_name_field().send_keys(user_name)

    def set_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)

    def set_confirm_password(self, confirm_password):
        self.get_confirm_password_field().clear()
        self.get_confirm_password_field().send_keys(confirm_password)

    def click_register_button(self):
        self.get_register_button().click()
