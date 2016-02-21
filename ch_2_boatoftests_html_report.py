'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.4
    ch_2
'''

import unittest
import HTMLTestRunner
import os, sys
from ch_2_searching_class_methods import SearchTests
from ch_2_german_version import GermanLangTest
from ch_2_searching import SearchTests as ST
from ch_3_different_selectors import DiffSelectors as DS
from ch_4_googling import NavigationTest as NT
from ch_4_registration import RegisterNewUser as RU
from ch_5_alerts import AlertTest

def get_tests():
    # get all tests
    search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
    german_ver = unittest.TestLoader().loadTestsFromTestCase(GermanLangTest)
    searching = unittest.TestLoader().loadTestsFromTestCase(ST)
    different_selectors = unittest.TestLoader().loadTestsFromTestCase(DS)
    googling = unittest.TestLoader().loadTestsFromTestCase(NT)
    registration = unittest.TestLoader().loadTestsFromTestCase(RU)
    alerts = unittest.TestLoader().loadTestsFromTestCase(AlertTest)


    # create a test suite
    boat_of_tests = unittest.TestSuite(
            [search_tests, german_ver, searching, different_selectors, googling, registration, alerts])
    return boat_of_tests


def run_tests(all_tests):
    # get the directory path to output report file
    result_dir = os.getcwd()
    unittest.TextTestRunner(verbosity=2)
    # open the report file
    outfile = open(result_dir + '\Boat_Tests_Report.html', 'w')
    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                           title='Test Report',
                                           description='Boat Of The Tests')
    # run the suite
    runner.run(all_tests)

if __name__ == '__main__':
    user_input = input('Create HTML report ??? yes(y)/no(n)   : ').lower()
    tests = get_tests()
    if user_input == 'y':
        run_tests(tests)
    elif user_input == 'n':
        unittest.TextTestRunner(verbosity=2).run(tests)
    else:
        sys.stdout.write("! Invalid input ! -  " + user_input)
