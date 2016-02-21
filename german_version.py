'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.4
    ch_2
'''

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GermanLangTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application start page
        cls.driver.get('http://demostore.x-cart.com')

    def test1_search_field(self):
        # check search field exists on the page
        self.assertTrue(self.is_element_present(By.ID, 'substring-default'))

    def test2_language_dropdown(self):
        # check language options dropdown on the page
        self.assertTrue(self.is_element_present(By.XPATH, '//span[@class="lng"]'))
        dropdown = self.driver.find_element_by_xpath('//li[@class="language-selector"]/ul')
        de_lang = self.driver.find_element_by_xpath('//li[@class="not-current"]/a/span[text()="de"]')
        hover = ActionChains(self.driver).move_to_element(dropdown).move_to_element(de_lang)
        hover.click().perform()

    def test3_german_page_assert(self):
        # check content on German version
        check_list = ['Verkaufsschlager','Neuankömmlinge','Kategorien',\
                      'Demnächst verfügbar','Vorgestellte Produkte','Ausverkauf']
        assert(self.driver.find_element_by_xpath('//a[@class="register"]').text) == 'Registrierung'
        for each in self.driver.find_elements_by_xpath("//div[@class='head-h2']"):
            assert(each.text in check_list)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)