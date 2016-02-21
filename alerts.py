"""
    File name : alerts
    Author : Aleksander Boldyrev
    Python Version: 3.4
    IDE : PyCharm Community Edition
    ch_5
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import unittest


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://the-internet.herokuapp.com/')

    def test_js_alert(self):
        # click the JavaScript Alerts to open test-page
        self.driver.find_element_by_link_text('JavaScript Alerts').click()

        # wait for Alert Button to be visible
        confirm_button = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located(
                (By.XPATH, "//li/button[text()='Click for JS Confirm']")))

        # click on Alert Button,
        # this will display an alert to the user
        confirm_button.click()

        # wait for the alert to present
        alert = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.alert_is_present())

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual('I am a JS Confirm', alert_text)
        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
