from selenium import webdriver
from selenium.webdriver.common.by import By
from math import radians, cos, sin, asin, sqrt



driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.learnwebservices.com/locations/server')

id_velence = driver.find_element(By.XPATH, "//tr[td[text() = 'Velence']]/td[1]").text
id_bata = driver.find_element(By.XPATH, "//tr[td[text() = 'Báta']]/td[1]").text
sum_vel_bata = int(id_bata) + int(id_velence)
print(sum_vel_bata)

name_first = driver.find_element(By.XPATH, "//tr[td[text() = '9876']]/td[2]").text
print(name_first[:3])

name_sec = driver.find_element(By.XPATH, "//tr[td[text() = '9742']]/td[2]").text
print(len(name_sec))
print(name_first[::-1])

name_thi = driver.find_element(By.XPATH, "//tr[td[text() = '11115']]/td[2]").text
print(name_thi.upper())
print(name_thi.lower())

name_11116 = driver.find_element(By.XPATH, "//tr[td[text() = '11116']]/td[2]").text
name_11117 = driver.find_element(By.XPATH, "//tr[td[text() = '11117']]/td[2]").text
name_11118 = driver.find_element(By.XPATH, "//tr[td[text() = '11118']]/td[2]").text

print(name_11116)
print(name_11117)
print(name_11118)

print(name_11116+"-"+name_11117+"-"+name_11118)

coord_tol = driver.find_element(By.XPATH, "//tr[td[text() = 'Tolmács']]/td[3]").text
coord_tol_re = coord_tol.replace(",", " ")
coord_tol_rep = coord_tol_re.replace(".", ",")
print(coord_tol_rep)

coord_tiszak = driver.find_element(By.XPATH, "//tr[td[text() = 'Tiszakerecseny']]/td[3]").text.split(",")
coord_tiszar = driver.find_element(By.XPATH, "//tr[td[text() = 'Tiszarád']]/td[3]").text.split(",")

lat1 = float(coord_tiszak[0])
lon1 = float(coord_tiszak[1])
lat2 = float(coord_tiszar[0])
lon2 = float(coord_tiszar[1])

print(lat1)
print(lat2)
print(lon1)
print(lon2)

lat = lat1 - lat2
lon = lon1 - lon2
print(lat)
print(lon)


coord_id_tel = driver.find_element(By.XPATH, "//tr[td[text() = '11262']]/td[2]").text
print("margit" in coord_id_tel)




def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

print(haversine(lon1, lat1, lon2, lat2))


driver.quit()
