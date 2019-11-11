import time
from test.ttt import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.learnwebservices.com/locations/server');
ts = time.time()
name = "bb" + str(ts)
driver.find_element_by_name("name").send_keys(name)
driver.find_element_by_name("coords").send_keys("10,10")
button = driver.find_element_by_xpath("//html/body/div/form/button")
button.click()
driver.find_element_by_xpath("//tr[td[text() = " + '${name}'+ "]]//a").click()

time.sleep(4)

driver.quit()