'''
    File name : different_selectors
    Author : Aleksander Boldyrev
    Python Version: 3.4
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class DiffSelectors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://demostore.x-cart.com')

    def test1_search_field_max_length(self):
        # get the search textbox
        search_field = self.driver.find_element_by_id('substring-default')
        # check maxlength attribute is set to 128
        self.assertEqual('255', search_field.get_attribute("maxlength"))

    def test2_search_button_enabled(self):
        # get Search button
        search_button = self.driver.find_element_by_css_selector('.btn.regular-button.submit-button.submit')
        # check Search button is enabled
        self.assertTrue(search_button.is_enabled())

    def test3_shipping_link_is_dispalyed(self):
        # get the shipping link
        shipping_link = self.driver.find_element_by_link_text('Shipping')
        # check Shipping link is displayed
        self.assertTrue(shipping_link.is_displayed())

    def test4_count_menu_items(self):
        # get top menu items
        menu_items = self.driver.find_elements_by_xpath("//*[@class='nav navbar-nav mm-listview']/li")
        # count top menu items
        self.assertEqual(6, len(menu_items))

    def test5_count_promo_banners(self):
        # get promo banner images
        promo = self.driver.find_element_by_class_name('carousel-inner')
        promo_imgs = promo.find_elements_by_tag_name('img')
        # count banners
        self.assertEqual(3, len(promo_imgs))

    def test6_navigate_sale_page(self):
        # get sale item from menu
        sale_butt = self.driver.find_element_by_xpath\
            ("//div[@id='page']/div[@class='navbar navbar-inverse mobile-hidden']//span[text()='Sale']")
        self.assertTrue(sale_butt.is_displayed())
        sale_butt.click()
        self.assertEqual("Sale", self.driver.title)
        self.assertEqual("Sale", self.driver.find_element_by_id('page-title').text)


    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
