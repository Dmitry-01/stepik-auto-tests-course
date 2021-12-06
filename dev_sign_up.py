import traceback
from telnetlib import EC

import action as action
from selenium import webdriver
from random import *
import time
import requests
from pymongo import MongoClient
from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from storage_mongo import MongoStorage

link2 = "https://prosto.ru"
a = str(randint(1, 99999))
nm = ("test" + a)
email_string = ("d.serakov" + a + "@gamil.com")

MONGO_URI = "123.2.345.36."
DB_NAME = "name"
COLLECTION_NAME = "user"

storage = MongoStorage(
    mongo_uri=MONGO_URI,
    db_name=DB_NAME,
    collection_name=COLLECTION_NAME
)

# try:
browser = webdriver.Chrome()
browser.get(link2)
time.sleep(10)


input1 = browser.find_element_by_name("name")
input1.send_keys(nm)

input1 = browser.find_element_by_name("email")
input1.send_keys(email_string)

input2 = browser.find_element_by_name("password")
input2.send_keys("+erferfererferfefe@g,ail.com")

#     input4 = browser.find_element_by_id("phone-form-control")
#     input4.send_keys("452532352")
#     input5 = browser.find_element_by_name("info.socialNetwork")
#     input5.send_keys("linkedin.com/in/john-doe-123456789")
#     input6 = browser.find_element_by_name("checkbox")
#     input6.click()
#     input7 = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/button")
#     input7.click()
#
#     time.sleep(5)
#
#     code = storage.get_code(email_string)
#     print(code)
#
#     input_code1 = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[1]/div/div[1]/input")
#     input_code1.send_keys(code[0])
#     input_code2 = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[1]/div/div[2]/input")
#     input_code2.send_keys(code[1])
#     input_code3 = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[1]/div/div[3]/input")
#     input_code3.send_keys(code[2])
#     input_code3 = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[1]/div/div[4]/input")
#     input_code3.send_keys(code[3])
#
#     button_send = browser.find_element_by_tag_name("button").click()
#
#     time.sleep(5)
#
#     input_companyname = browser.find_element_by_name("company")
#     input_companyname.send_keys("Auto-test")
#     input_position = browser.find_element_by_name("position")
#     input_position.send_keys("QA Automation")
#
#     input_namber_of_emp = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[3]/div[2]/div[1]/div").click()
#     input_field_of_activity = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[4]/div[2]/div[1]/div").click()
#     input_platforms = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/div/div/auth2/form/div[5]/div[2]/div[1]/div").click()
#
#     button_next = browser.find_element_by_tag_name("button").click()
#
#     time.sleep(120)
#     element = browser.find_element_by_xpath("/html/body/div[7]/div/div/div/button")
#     element.click()
#
#
#     element1 = browser.find_element_by_id("desktopUserMenu-dropStretch")
#     element1.click()
#
#
#     element2 = browser.find_element_by_xpath("//a[@href='/settings/subscriptions']")
#     element2.click()
#     time.sleep(30)
#
#     element3 = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/checkout?key=startup_year']")
#     element3.click()
#     time.sleep(5)
#
#     billing_date_individual = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/div/payment/div[2]/div[1]/div[2]/div/form/div/div/div[2]/div").click()
#
#     time.sleep(10)
#     country = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/div/payment/div[2]/div[1]/div[2]/div/form[2]/div[1]/div[5]/div/div[2]/div")
#     country.click()
#
#
#     browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/div/payment/div[2]/div[1]/div[2]/div/form[2]/div[1]/div[5]/div/div[2]/div[2]/div/button/div[text()='{0}']".format('France')).click()
#
#
#     city = browser.find_element_by_name("address.city")
#     city.send_keys("Paris")
#
#     billing_adress = browser.find_element_by_name("address.line1")
#     billing_adress.send_keys("Pantin 4")
#
#     index = browser.find_element_by_name("address.postal_code")
#     index.send_keys("75056")
#
#     button_save = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/div/payment/div[2]/div[1]/div[2]/div/form[2]/div[2]/button[1]")
#     button_save.click()
#
#     browser.find_element_by_xpath("//*[@id='lskform_number']/div/input").send_keys("4242424242424242")
#
#     browser.find_element_by_xpath("//*[@id='lskform_expired']/div/input").send_keys("1225")
#
#     browser.find_element_by_xpath("//*[@id='lskform_cvc']/div/input").send_keys("322")
#
#     browser.find_element_by_xpath("//*[@id='lskform_fullName']/div/input").send_keys("Dima Serakov")
#
#     time.sleep(15)
#
#     button_save = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[1]/div/payment/div[2]/div[2]/div[2]/div/form/div[2]/button[2]")
#     button_save.click()
#     time.sleep(15)
#
#     pay = browser.find_element_by_xpath("/ html / body / div[1] / main / section / div / div[1] / div[2] / article / div / div / form / div / button")
#     pay.click()
#     time.sleep(30)
#
#     button_success = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/edit']")
#     button_success.click()
#     time.sleep(30)
#     change_button = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans']")
#     change_button.click()
#
#     time.sleep(60)
#     change_to_company = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/checkout?key=company_year']")
#     change_to_company.click()
#     time.sleep(30)
#
#     pay_button = browser.find_element_by_xpath("/html/body/div[1]/main/section/div/div[1]/div[2]/article/div/div/form/div/button")
#     pay_button.click()
#     time.sleep(30)
#     button_success1 = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/edit']")
#     button_success1.click()
#     time.sleep(30)
#
# #     Покупаем тариф Enterprise
#     change_to_button2 = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans']")
#     change_to_button2.click()
#     time.sleep(30)
#
#     change_to_enterprise = browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/checkout?key=enterprise_year']")
#     change_to_enterprise.click()
#     time.sleep(30)
#
#     pay_button3 = browser.find_element_by_xpath('/html/body/div[1]/main/section/div/div[1]/div[2]/article/div/div/form/div/button')
#     pay_button3.click()
#
#     time.sleep(30)
#
#     button_success_entpr =browser.find_element_by_xpath("//a[@href='/settings/subscriptions/plans/edit']")
#     button_success_entpr.click()
#     time.sleep(15)
#
# #     И переходим на таблицу блогеровя
#     influencer_button =browser.find_element_by_xpath("//a[@href='/youtube/channels']")
#     influencer_button.click()
#
# except Exception as e:
#     print(traceback.format_exc())
#
# finally:
#     #     # успеваем скопировать код за 30 секунд
#     #     time.sleep(30)
#     #     # закрываем браузер после всех манипуляций
#     # browser.quit()
#     print('Регистрация и покупка тарифов завершена успешна')
