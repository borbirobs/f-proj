from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.learnwebservices.com/locations/server')

coordinates = driver.find_element(By.XPATH, "//tr[td[text() = 'Dobogókő']]/td[2]").text
print(coordinates)
print(type(coordinates))

al = driver.find_element(By.XPATH, "//tr[td[text() = 'Alattyán']]/td[1]").text
print(al)
print(type(al))

coordinates_type = driver.find_element(By.XPATH, "//tr[td[text() = '9277']]/td[2]").text
print(coordinates_type)
print(type(coordinates_type))

coordinates_type_bakony_bank = driver.find_element(By.XPATH, "//tr[td[text() = 'Bakonybánk']]/td[1]").text
print(coordinates_type_bakony_bank)
print(type(coordinates_type_bakony_bank))
coordinates_type_bakony_bank_new_type = int(coordinates_type_bakony_bank)
print(type(coordinates_type_bakony_bank_new_type))


coordinates_type_zsambek = driver.find_element(By.XPATH, "//tr[td[text() = 'Zsámbék']]/td[3]").text
print(coordinates_type_zsambek)
print(type(coordinates_type_zsambek))
#balró zárt jobbról nyitott az intervallum
print("Agyagosszergény"[3:6])
print("Agyagosszergény"[0:3])
#ha nem adod meg az automatikusan azt jelenti, hogy a 0tól
print("Agyagosszergény"[:3])
#ha nem adod meg a végét, akkor a végéig. hány karakterenként(lépés)
print("Agyagosszergény"[2:10:2])
#elejétől a végéig, visszafele
print("Agyagosszergény"[::-1])
print("Agyagosszergény"[14:8:-1])
#mit cserél mire
print("Agyagosszergény".replace("A", "E"))
print("Agyagosszergény".upper())
print("agy" in "Agyagosszergény".lower())

line = "Windows 2000;Windows Server 2000;kétezer"
parts = line.split(";")
print(parts[0])
print(parts[1])
print(parts[2])






#coordinates_type_zsambek_new_type = float(coordinates_type_zsambek)
#print(type(coordinates_type_zsambek_new_type))




driver.quit()
