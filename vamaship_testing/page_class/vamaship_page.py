# __author__ = 'hafsa'

from selenium.webdriver.common.by import By

from .page_base import AbstractBasePage


class VamashipPage(AbstractBasePage):

    _LOGIN_BUTTON_LOCATOR = (By.ID, 'login-icon')
    _LOGIN_EMAIL_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#email')
    _LOGIN_PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#password')
    _LOGIN_SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[value="LOGIN"]')

    _CREATE_NAV_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.personal-shipments-nav a')
    _ORIGIN_PINCODE_INPUT_LOCATOR = (By.CSS_SELECTOR, '[list="origin_pincodes"]')
    _DESTINATION_PINCODE_INPUT_LOCATOR = (By.CSS_SELECTOR, '[list="detination_pincodes"]')
    _SHIPMENT_DATEPICKER_LOCATOR = (By.CLASS_NAME, 'input-group-addon')
    _SHIPMENT_DATE_OPTION_LOCATOR = (By.CSS_SELECTOR, '.today.day')
    _SHIPMENT_WEIGHT_INPUT_LOCATOR = (By.ID, 'weight-air-intl')

    _PACKAGE_LENGTH_INPUT_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Length"]')
    _PACKAGE_WIDTH_INPUT_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Width"]')
    _PACKAGE_HEIGHT_INPUT_LOCATOR = (By.CSS_SELECTOR, '[placeholder="Height"]')
    _PACKAGE_DIMENSION_UNIT_LOCATOR = (By.CSS_SELECTOR, '.unit .btn-primary:not(.active)')

    _COD_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#paytyp-buttons label')
    _PRODUCT_VALUE_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name="pv"]')
    _COD_VALUE_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name="codv"]')

    _CREATE_SHIPMENT_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[value="Create Shipment"]')
    _CONTINUE_ORDER_BTN_LOCATOR = (By.CSS_SELECTOR, 'button.gotonext')

    _ORIGIN_NAME_INPUT_LOCATOR = (By.ID, 'from_name')
    _ORIGIN_EMAIL_INPUT_LOCATOR = (By.ID, 'from_email')
    _ORIGIN_MOBILE_INPUT_LOCATOR = (By.ID, 'from_contact')
    _ORIGIN_ADDRESS_INPUT_LOCATOR = (By.ID, 'from_address_1')
    _ORIGIN_STREET_INPUT_LOCATOR = (By.ID, 'from_address_2')
    _ORIGIN_AREA_INPUT_LOCATOR = (By.ID, 'from_address_3')

    _DESTINATION_NAME_INPUT_LOCATOR = (By.ID, 'to_name')
    _DESTINATION_EMAIL_INPUT_LOCATOR = (By.ID, 'to_email')
    _DESTINATION_MOBILE_INPUT_LOCATOR = (By.ID, 'to_contact')
    _DESTINATION_ADDRESS_INPUT_LOCATOR = (By.ID, 'to_address_1')
    _DESTINATION_STREET_INPUT_LOCATOR = (By.ID, 'to_address_2')
    _DESTINATION_AREA_INPUT_LOCATOR = (By.ID, 'to_address_3')

    _PRODUCT_DESCRIPTION_INPUT_LOCATOR = (By.ID, 'product')
    _ACCEPT_T_N_C_INPUT_LOCATOR = (By.ID, 'accept_tnc')

    _CONTINUE_TO_PAYMENT_BTN_LOCATOR = (By.CSS_SELECTOR, 'input.gotonext')

    def click_on_header_login_btn(self):
        return self.click_on_element(self._LOGIN_BUTTON_LOCATOR)

    def fill_user_email_id(self, email):
        return self.enter_field_input(self._LOGIN_EMAIL_INPUT_LOCATOR, email)

    def fill_user_password(self, p_word):
        return self.enter_field_input(self._LOGIN_PASSWORD_INPUT_LOCATOR, p_word)

    def click_on_submit_login_btn(self):
        return self.click_on_element(self._LOGIN_SUBMIT_BUTTON_LOCATOR)

    def login_user(self, email, p_word):
        result1 = self.fill_user_email_id(email)
        result2 = self.fill_user_password(p_word)
        result3 = self.click_on_submit_login_btn()
        return result1 and result2 and result3

    def click_on_create_button(self):
        return self.click_on_element(self._CREATE_NAV_BUTTON_LOCATOR)

    def check_shipment_page_is_current_page(self):
        return self.check_for_new_url('personal-shipments')

    def fill_origin_pincode(self):
        return self.enter_field_input(self._ORIGIN_PINCODE_INPUT_LOCATOR, '400001')

    def fill_destination_pincode(self):
        return self.enter_field_input(self._DESTINATION_PINCODE_INPUT_LOCATOR, '400093')

    def select_shipment_date(self):
        result_1 = self.click_on_element(self._SHIPMENT_DATEPICKER_LOCATOR)
        result_2 = self.click_on_element(self._SHIPMENT_DATE_OPTION_LOCATOR)
        return result_1 and result_2

    def fill_shipment_weight(self):
        return self.enter_field_input(self._SHIPMENT_WEIGHT_INPUT_LOCATOR, '20')

    def fill_package_dimensions(self):
        result1 = self.enter_field_input(self._PACKAGE_LENGTH_INPUT_LOCATOR, '2')
        result2 = self.enter_field_input(self._PACKAGE_WIDTH_INPUT_LOCATOR, '3')
        result3 = self.enter_field_input(self._PACKAGE_HEIGHT_INPUT_LOCATOR, '4')
        return result1 and result2 and result3

    def select_inches_unit(self):
        return self.click_on_element(self._PACKAGE_DIMENSION_UNIT_LOCATOR)

    def select_cod_option(self):
        self.scroll_into_view(self._COD_BUTTON_LOCATOR, 1)
        return self.click_on_element(self._COD_BUTTON_LOCATOR, 1)

    def fill_product_value(self):
        return self.enter_field_input(self._PRODUCT_VALUE_INPUT_LOCATOR, '20000')

    def fill_cod_value(self):
        return self.enter_field_input(self._COD_VALUE_INPUT_LOCATOR, '100')

    def click_on_create_shipment_btn(self):
        return self.click_on_element(self._CREATE_SHIPMENT_BUTTON_LOCATOR)

    def click_on_continue_order_btn(self):
        return self.click_on_element(self._CONTINUE_ORDER_BTN_LOCATOR)

    def fill_origin_details(self):
        self.enter_field_input(self._ORIGIN_NAME_INPUT_LOCATOR, 'XYZ Test')
        self.enter_field_input(self._ORIGIN_EMAIL_INPUT_LOCATOR, 'xyz@test.com')
        self.enter_field_input(self._ORIGIN_MOBILE_INPUT_LOCATOR, '8796059100')
        self.enter_field_input(self._ORIGIN_ADDRESS_INPUT_LOCATOR, 'xyz address')
        self.enter_field_input(self._ORIGIN_STREET_INPUT_LOCATOR, 'xyz street')
        self.enter_field_input(self._ORIGIN_AREA_INPUT_LOCATOR, 'xyz area')

    def fill_destination_details(self):
        self.enter_field_input(self._DESTINATION_NAME_INPUT_LOCATOR, 'abc Test')
        self.enter_field_input(self._DESTINATION_EMAIL_INPUT_LOCATOR, 'abc@test.com')
        self.enter_field_input(self._DESTINATION_MOBILE_INPUT_LOCATOR, '8796059100')
        self.enter_field_input(self._DESTINATION_ADDRESS_INPUT_LOCATOR, 'abc address')
        self.enter_field_input(self._DESTINATION_STREET_INPUT_LOCATOR, 'abc street')
        self.enter_field_input(self._DESTINATION_AREA_INPUT_LOCATOR, 'abc area')

    def fill_product_description(self):
        return self.enter_field_input(self._PRODUCT_DESCRIPTION_INPUT_LOCATOR,
                                      'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. '
                                      'Aenean commodo ligula eget dolor')

    def accept_terms_and_conditions(self):
        return self.click_on_element(self._ACCEPT_T_N_C_INPUT_LOCATOR)

    def click_on_continue_to_payment_btn(self):
        return self.click_on_element(self._CONTINUE_TO_PAYMENT_BTN_LOCATOR)
