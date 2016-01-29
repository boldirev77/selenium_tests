'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.3
'''

import unittest
import HTMLTestRunner
import os
from searching_class_methods import SearchTests
from german_version import GermanLangTest

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
german_ver = unittest.TestLoader().loadTestsFromTestCase(GermanLangTest)

# create a test suite combining search_test and home_page_test
boat_of_tests = unittest.TestSuite([search_tests, german_ver])

# get the directory path to output report file
result_dir = os.getcwd()
# open the report file
outfile = open(result_dir + '\Boat_Tests_Report.html', 'w')
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       title='Test Report',
                                       description='Boat Of The Tests')

# run the suite
runner.run(boat_of_tests)