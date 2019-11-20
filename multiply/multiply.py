from selenium import webdriver
from selenium.webdriver.common.by import By

def multiply_with_form(a, b):
    first = driver.find_element(By.ID, 'a-input').send_keys(a)
    second = driver.find_element(By.ID, 'b-input').send_keys(b)
    multiply = driver.find_element(By.ID, 'calculate-button').click()
    result = driver.find_element(By.ID, "result-div").text
    print(result)
    return  int(result)


def multiply_with_table(a, b):
    xpath_first = "//tr[1]/td[number]".replace("number", str(a))
    xpath_second = "//tr[number]/td[1]".replace("number", str(b))


    xpath = "//tr[number1]/td[number2]".replace("number1", str(a)).replace("number2", str(b))
    number = driver.find_element(By.XPATH, xpath).text
    print(number)
    return int(number)



    #first = driver.find_element(By.XPATH, xpath_first)
    #second = driver.find_element(By.XPATH, xpath_second)

def multiply(a, b):
    multiply = int(a) * int(b)
    print(multiply)
    return int(multiply)


def mul(first, second):
    result_form = multiply_with_form(first, second)

    result_table = multiply_with_table(first, second)
    result_simple = multiply(first, second)

    if result_form == result_table and result_table == result_simple:
        print("Egyenlő")
    elif result_form == result_table or result_table == result_simple or result_simple == result_table:
        print("majdnemjó")
    else:
        print("nemegyenlő")

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html')

multiply_with_form(4,6)
multiply_with_table(6,5)
multiply(3,4)
mul(5,9)

# driver.close()