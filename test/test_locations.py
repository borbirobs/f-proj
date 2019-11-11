import time
from test.ttt import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.learnwebservices.com/locations/server');
driver.find_element_by_name("name").send_keys("")
driver.find_element_by_name("coords").send_keys("10,10")
button = driver.find_element_by_xpath("//html/body/div/form/button")
button.click()
assert "must not be blank" in driver.page_source

time.sleep(4)

driver.quit()
