from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://httpstatuses.com')


kod = input("Azonosító=")
print(kod)
xpath = "//a[contains(@href, '/"+kod+"')]"
print(xpath)
name_td = driver.find_element(By.XPATH, xpath).text
print(name_td)

driver.quit()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://httpstatusdogs.com')

xpathpicture = "//a[contains(@href, '"+kod+"')]/img"
print(xpathpicture)
picture = driver.find_element(By.XPATH, xpathpicture).screenshot('picture2.png')
driver.quit()

