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

# исправил    nj k
