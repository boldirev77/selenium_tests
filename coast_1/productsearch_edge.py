'''
    File name: 
    Author: Aleksander Boldyrev
    Python Version: 3.4
'''

from selenium import webdriver

# get the path of IEDriverServer

Edge_driver_path = "d:\Selenium" + "\mswd\MicrosoftWebDriver.exe"

# create a new Firefox session
driver = webdriver.Edge(Edge_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('http://demostore.x-cart.com')

# get the search textbox
search_field = driver.find_element_by_id('substring-default')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('robot')
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//div[@class='head-h3 product-name']/a")

# get the number of anchor elements found
print('Found ' + str(len(products)) + ' products:')

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print(products.index(product) + 1, '--', product.text)

# close the browser window
driver.quit()
