from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://borbirobs.github.io/f-proj/')
# driver.find_element_by_name("a").send_keys("2")

first_number=input("a=")
print(first_number)
second_number=input("b=")
print(second_number)

res_con = int(first_number) + int(second_number)

print(res_con)

first_input_field = driver.find_element_by_name("a")
first_input_field.send_keys(first_number)
#first_input_field.screenshot("first-input.png")

driver.find_element_by_name("b").send_keys(second_number)
driver.find_element_by_id("submit-button").click()
result = driver.find_element_by_id("result-input").get_attribute("value")
print(result)

print(type(res_con))
print(type(result))

assert int(result) == res_con

driver.save_screenshot("result.png")
header_text = driver.find_element_by_xpath("//h1").text
print(header_text)
assert header_text == "Számológép"




print("hello")
driver.close()
