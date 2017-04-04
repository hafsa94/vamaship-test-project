from random import randint
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractBasePage(object):

    PATH = '/'

    _timeout = 30
    MAIN_URL = 'https://www.vamaship.com'

    def __init__(self, *args):
        """ Initializer method for Page base """
        self._base_url = self.MAIN_URL
        # Waring!
        #   Variable 'selenium' is not an object of Selenium class
        #   It is a Selenium Webdriver Object!

        self.selenium = args[0]

    def click_on_element(
            self,
            locator,
            index=None):
        click_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator))
            WebDriverWait(self.selenium, self._timeout).until(
                EC.element_to_be_clickable(locator))

            button_link = self.selenium.find_elements(*locator)

            if index is None:
                if len(button_link) > 1:
                    index = randint(0, len(button_link) - 1)
                else:
                    index = 0

            time.sleep(3)
            button_link[index].click()
            click_result = True

        finally:
            # return True
            return click_result

    def enter_field_input(
            self,
            input_locator,
            values="No Input"):
        fill_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(input_locator))
            WebDriverWait(self.selenium, self._timeout).until(
                EC.visibility_of_element_located(input_locator))

            name_field = self.selenium.find_element(*input_locator)

            time.sleep(3)

            name_field.send_keys(Keys.CONTROL + 'a')
            name_field.send_keys(Keys.BACKSPACE)

            name_field.send_keys(str(values))

            fill_result = True

        finally:
            return fill_result

    def check_for_new_url(
            self,
            expected_url_string):
        check_result = False
        time.sleep(3)
        current_page_url = str(self.selenium.current_url)
        if expected_url_string in current_page_url:
            check_result = True
        return check_result

    def go_to_page(self):
        url = self._base_url + self.PATH
        # print("\nURL -=> ", url)
        self.selenium.get(url)

    def refresh(self):
        self.selenium.refresh()

    def maximize(self):
        self.selenium.maximize_window()

    def scroll_into_view(self, locator, index=0, scroll_val=100):
        WebDriverWait(self.selenium, self._timeout).until(
            EC.presence_of_element_located(locator))
        WebDriverWait(self.selenium, self._timeout).until(
            EC.visibility_of_element_located(locator))
        elems = self.selenium.find_elements(*locator)
        self.selenium.execute_script("return arguments[0].scrollIntoView();", elems[index])
        self.selenium.execute_script("window.scrollBy(0, -" + str(scroll_val) + ");")
