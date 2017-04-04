import nose.tools
import nose.plugins.multiprocess
from nose.plugins.attrib import attr

import time

from test_base import BaseTest
from page_class.vamaship_page import VamashipPage


# @attr()
# @attr(type="run")
class TestVamashipPage(BaseTest):

    _multiprocess_can_split_ = True

    prod_test = True

    _EMAIL = 'softwaretester@its4solutions.com'
    _PASSWORD = 'v@mas#1P&t9$^'

    @classmethod
    def setUpClass(self):
        super(TestVamashipPage, self).setUpClass()
        self.vamaship_page = VamashipPage(self._browser)
        self.vamaship_page.go_to_page()
        self.vamaship_page.maximize()

    def test_01_check_header_login_btn_working(self):
        nose.tools.assert_true(self.vamaship_page.click_on_header_login_btn())

    def test_02_check_user_is_logged_in_successfully(self):
        nose.tools.assert_true(self.vamaship_page.login_user(self._EMAIL, self._PASSWORD))

    def test_03_check_create_btn_working(self):
        nose.tools.assert_true(self.vamaship_page.click_on_create_button())

    def test_04_check_shipment_page_is_current_page(self):
        nose.tools.assert_true(self.vamaship_page.check_shipment_page_is_current_page())

    def test_05_fill_origin_pincode(self):
        nose.tools.assert_true(self.vamaship_page.fill_origin_pincode())

    def test_06_fill_destination_pincode(self):
        nose.tools.assert_true(self.vamaship_page.fill_destination_pincode())

    def test_08_select_shipment_date(self):
        nose.tools.assert_true(self.vamaship_page.select_shipment_date())

    def test_09_fill_shipment_weight(self):
        nose.tools.assert_true(self.vamaship_page.fill_shipment_weight())

    def test_10_fill_package_dimensions(self):
        nose.tools.assert_true(self.vamaship_page.fill_package_dimensions())

    def test_11_select_inches_unit(self):
        nose.tools.assert_true(self.vamaship_page.select_inches_unit())

    def test_12_select_cod_option(self):
        nose.tools.assert_true(self.vamaship_page.select_cod_option())

    def test_13_fill_product_value(self):
        nose.tools.assert_true(self.vamaship_page.fill_product_value())

    def test_14_fill_cod_value(self):
        nose.tools.assert_true(self.vamaship_page.fill_cod_value())

    def test_15_click_on_create_shipment_btn(self):
        nose.tools.assert_true(self.vamaship_page.click_on_create_shipment_btn())

    def test_16_click_on_continue_order_btn(self):
        nose.tools.assert_true(self.vamaship_page.click_on_continue_order_btn())

    def test_17_fill_origin_details(self):
        self.vamaship_page.fill_origin_details()

    def test_18_fill_destination_details(self):
        self.vamaship_page.fill_destination_details()

    def test_19_fill_product_details(self):
        nose.tools.assert_true(self.vamaship_page.fill_product_description())

    def test_20_accept_terms_and_conditions(self):
        nose.tools.assert_true(self.vamaship_page.accept_terms_and_conditions())

    def test_21_click_on_continue_to_payment_btn(self):
        nose.tools.assert_true(self.vamaship_page.click_on_continue_to_payment_btn())
        time.sleep(5)