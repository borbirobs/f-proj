from selenium import webdriver
from selenium.webdriver.common.by import By

def print_coords_by_name(name):
    xpath = "//tr[td[text() = 'name']]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)

def print_id_by_name(name):
    xpath = "//tr[td[text() = 'name']]/td[1]".replace("name", name)
    id = driver.find_element(By.XPATH, xpath).text
    print(id)


def print_name_by_id(id):
    xpath = "//tr[td[text() = 'id']]/td[2]".replace("id", id)
    name2 = driver.find_element(By.XPATH, xpath).text
    print(name2)

def print_coord_by_id(id):
    xpath = "//tr[td[text() = 'id']]/td[3]".replace("id", id)
    coord = driver.find_element(By.XPATH, xpath).text
    print(coord)

def new_fav(name, coord):
    name_field = driver.find_element(By.XPATH, '//[@id="nameInput"]')
    coord_field = driver.find_element(By.XPATH, '//[@id="coordsInput"]')
    name_field.send_keys(name)
    coord_field.send_keys(coord)
    driver.find_element(By.XPATH, '/html/body/div/form/button').click()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.learnwebservices.com/locations/server')


print_coords_by_name("Abasár")
print_id_by_name("Abádszalók")
print_name_by_id("8463")
print_coord_by_id("8463")
new_fav("Varso", "20,30")



driver.quit()