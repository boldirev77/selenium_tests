"""
    File name : registration
    Author : Aleksander Boldyrev
    Python Version: 3.4
    ch_4
"""
from selenium import webdriver
import unittest
import os

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        chrome_driver_path = os.path.dirname(__file__) + "\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the home page
        self.driver.get('http://demostore.x-cart.com')

    def test1_new_user(self):
        self.driver.find_element_by_link_text("Register").click()
        create_button = self.driver.find_element_by_xpath('//div[@class="button submit"]/button')
        # check Create button is displayed and enabled
        self.assertTrue(create_button.is_displayed() and create_button.is_enabled())
        # get input fields
        email_field = self.driver.find_element_by_id('login')
        pass_field = self.driver.find_element_by_id('password')
        pass_confirm = self.driver.find_element_by_id('password-conf')
        # max length field assertion
        self.assertEqual('128', email_field.get_attribute('maxlength'))
        self.assertEqual('255', pass_field.get_attribute('maxlength'))
        self.assertEqual('255', pass_confirm.get_attribute('maxlength'))
        # fill in the registration form
        email_text = 'test_user@test.com'
        email_field.clear()
        email_field.send_keys(email_text)
        pass_field.clear()
        pass_field.send_keys('test1')
        pass_confirm.clear()
        pass_confirm.send_keys('test1')
        # submit registration
        create_button.click()
        # verification whether the registration has been passed
        my_account = self.driver.find_element_by_xpath('//*[@id="header-bar"]//span[@class="email"]')
        self.assertEqual('('+email_text+')', my_account.text)

        # deleteting user
        detail_button = self.driver.find_element_by_xpath('//*[@class="page-tabs"]/ul/li/a[text()="Details"]')
        detail_button.click()
        delete_button = self.driver.find_element_by_xpath('//div[@class="button delete_profile"]/a')
        delete_button.click()
        # time.sleep(5)
        delete_confirm = self.driver.find_element_by_xpath(
                "//div[@class='delete-user-buttons-list']/button[@type='submit']")
        delete_confirm.click()
        # time.sleep(5)
        # check that we return to the home page
        self.driver.find_element_by_link_text("Register")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

