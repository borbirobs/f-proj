from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://borbirobs.github.io/f-proj/cica/triangles.html')




def szamol(a, b, c):
        a_input = driver.find_element(By.ID, "a-input");
        a_input.send_keys(a);

        b_input = driver.find_element(By.ID, "b-input");
        b_input.send_keys(b);


        c_input = driver.find_element(By.ID, "c-input");
        c_input.send_keys(c);

        calculate_button = driver.find_element(By.ID, "calculate-button");
        calculate_button.click();

        li_text = driver.find_element_by_xpath("//li[last()]").text
        print(li_text)
        assert li_text == "a = 1, b = 1, c = 1: Egyenlő oldalú"
        driver.save_screenshot("result.png")

szamol(1,1,1)