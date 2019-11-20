from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches",['enable-automation']);
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

driver.get('http://www.learnwebservices.com/empapp/employees.xhtml')

def filter(word):
    search_field = driver.find_element(By.XPATH, "/html/body/div/form[2]/input[1]").send_keys(word)
    search_button = driver.find_element(By.XPATH, "/html/body/div/form[2]/input[2]").click()

# def delete(id):
#     table = driver.find_element_by_class_name('table-striped')
#     for row in table.find_elements_by_xpath(".//tr"):
#         id_value = row.find_element_by_xpath('//a')
    # print([td.text for td in row.find_elements_by_xpath(".//td[@class='dddefault'][1]"])
    #     print('cica'+str(id_value))


def change(lang):
    if lang == 'magyar':
        hun = driver.find_element_by_xpath("//*[@id='j_idt16']/a[1]").click()
    elif lang == 'eng':
        eng = driver.find_element_by_xpath('//*[@id="j_idt16"]/a[2]').click()
    else:
        print("semmi")


def create_emp(input_name):
    print('start')

    penisz = 'meresihiba'
    create_button = driver.find_element_by_xpath("//a[contains(text(),'Create employee')]")
    create_button.click()
    print('elsőszar')
    name_filed = driver.find_element(By.ID, "create-form:name-input").send_keys(input_name)
    print('masodikszar')
    # name_filed.send_keys('cica')

    print('harmadikszar')
    create_emp_button = driver.find_element_by_id('create-form:save-button')
    create_emp_button.click()
    print(input_name)
    print('cica')



def error_log():
    error = driver.find_element(By.XPATH, '//*[@id="create-form:name-form-group"]/span').text
    print(error)


def card(card):
    card = driver.find_element_by_id("create-form:card-number-input").send_keys(card)
    create_button = driver.find_element_by_id("create-form:save-button").click()


def mul(user_name, card_number):
    create_emp(user_name)
    card(card_number)


def change_old_to_new(old, new):
    old_name = driver.find_element(By.XPATH, "//tr[td[text() = 'cica')]]/td[1]").click()
    # old_name = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[9]/td[1]").click()

# create_emp('bb')
# card('asasasas')
change_old_to_new('cica', 'kutya')

# mul('cica', 'gfjhegfjhgfjhs')
# filter('János')

# change('magyar')
# card('gvhjkl56zuiokm')
#error_log()


#filter('János')
# delete('dbabf24a-4d85-4729-ae31-cbe4a47ae731')

#driver.close()