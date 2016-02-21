"""
    File name : test
    Project name : _projects_Python
    Author : Aleksander Boldyrev
    Python Version: 3.4
    IDE : PyCharm Community Edition
    date : 21.02.2016
"""

import os
from selenium import webdriver

# create new Edge session
dir = os.path.dirname(__file__)
edge_path = dir + "\MicrosoftWebDriver.exe"
driver = webdriver.Edge(edge_path)
driver.implicitly_wait(10)
# driver.maximize_window()

driver.get("https://www.freelancer.in/")

login_button = driver.find_element_by_class_name("LandingHeader-authBtn")
login_button.click()

driver.quit()
