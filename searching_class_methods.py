'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.4
    ch_2
'''

import unittest
from selenium import webdriver


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://demostore.x-cart.com')
        cls.driver.title

    def test1_search_one(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id('substring-default')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('robot')
        self.search_field.submit()

        # get the elements displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='head-h3 product-name']/a")
        self.assertEqual(7, len(products))

    def test2_search_two(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id('substring-default')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('Shirt')
        self.search_field.submit()

        # get the elements displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='head-h3 product-name']/a")
        self.assertEqual(3, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
