'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.4
    ch_2
'''

import unittest
from ch_2_searching_class_methods import SearchTests
from ch_2_german_version import GermanLangTest

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
german_ver = unittest.TestLoader().loadTestsFromTestCase(GermanLangTest)

# create a test suite combining search_test and home_page_test
boat_of_tests = unittest.TestSuite([search_tests, german_ver])

# run the suite
unittest.TextTestRunner(verbosity=2).run(boat_of_tests)