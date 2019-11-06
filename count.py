from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://borbirobs.github.io/f-proj/')
driver.find_element_by_name("a").send_keys("2")
driver.find_element_by_name("b").send_keys("2")
driver.find_element_by_xpath("/html/body/div/form/input[3]").click()
header_text = driver.find_element_by_xpath("//h1").text
print(header_text)
assert header_text == "Számológép"



print("hello")
driver.close()
