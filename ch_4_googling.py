"""
    File name : googling
    Author : Aleksander Boldyrev
    Python Version: 3.4
    ch_4


        note: ERROR occurs because of selenium issue
        http://stackoverflow.com/questions/34930634/python-selenium-compilation-error
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class NavigationTest(unittest.TestCase):
    def setUp(self):
        # create a new  session
        chrome_driver_path = os.path.dirname(__file__) + "\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get('http://www.google.com')

    def test_browser_navigation(self):
        #driver = self.driver
        # get the search textbox
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('selenium webdriver')
        search_field.submit()

        se_wd_link = self.driver.find_element_by_link_text('Selenium WebDriver')
        se_wd_link.click()
        self.assertTrue(WebDriverWait(self.driver, 10)
                        .until(EC.title_is('Selenium WebDriver')))

        self.driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10)
                        .until(EC.title_contains('selenium webdriver - ')))

        self.driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10)
                        .until(EC.title_is('Selenium WebDriver')))

        self.driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10)
                        .until(EC.title_is('Selenium WebDriver')))

    def tearDown(self):
        # close the browser window
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
