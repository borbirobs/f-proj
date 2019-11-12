from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://borbirobs.github.io/f-proj/cica/triangles.html')




def szamol(a, b, c):
  a_input = driver.find_element(By.ID, "a-input");
  a_input.send_keys(a);
  b_input = driver.find_element(By.ID, "b-input");
  b_input.send_keys(b);
  c_input = driver.find_element(By.ID, "c-input");
  c_input.send_keys(c);
  element = driver.find_element(By.ID, "calculate-button")
  actions = ActionChains(driver)
  actions.move_to_element(element).click_and_hold().perform()
  element = driver.find_element(By.CSS_SELECTOR, "html")
  actions = ActionChains(driver)
  actions.move_to_element(element).release().perform()
  driver.find_element(By.CSS_SELECTOR, "html").click()
  driver.find_element(By.ID, "calculate-button").click()
  li_text = driver.find_element_by_xpath("//ul[@id='result-ul']/li[last()]").text
  print(li_text)
  assert li_text == "a = 1, b = 1, c = 1: Egyenlő oldalú"
  driver.save_screenshot("result.png")

szamol(1,1,1);