from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://borbirobs.github.io/f-proj/cica/triangles.html')




def szamol(a, b, c, triangletype):
  a_input = driver.find_element(By.ID, "a-input");
  a_input.send_keys(a);
  b_input = driver.find_element(By.ID, "b-input");
  b_input.send_keys(b);
  c_input = driver.find_element(By.ID, "c-input");
  c_input.send_keys(c);
  calculate_button = driver.find_element(By.ID, "calculate-button")
  calculate_button.click()
  calculate_button.click()

  li_text = driver.find_element_by_xpath("//ul[@id='result-ul']/li[last()]").text
  print(li_text)

  expectedtext = "a = "+str(a)+", b = "+str(b)+", c = "+str(c)+": "+triangletype
  assert li_text == expectedtext
  driver.save_screenshot("result.png")
  # driver.refresh()

  a_input.clear()
  b_input.clear()
  c_input.clear()



szamol(1,1,1, "Egyenlő oldalú")
szamol(1,2,3, "Nem háromszög")
# szamol(8,5,5, "Egyenlő szárú")
# Az egyenlő szárú háromszöget is egyenlő oldalúnak számolja. ITT A HIBA!
szamol(8,6,5, "Általános")
