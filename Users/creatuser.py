from selenium import webdriver
import time
from selenium.webdriver.common.by import By

host = "https://beta.hi-tech.org/administration.html#domainUsers:6a310898-e3a7-4562-9b6b-995b7f9fff17"
login=""
password=""

#Войти в администрирование
browser = webdriver.Chrome()
browser.get(host)
input1 = browser.find_element_by_xpath('//input[@type="text"]')
input1.send_keys(login)
input2 = browser.find_element_by_xpath('//input[@type="password"]')
input2.send_keys(password)
button = browser.find_element_by_css_selector("div>:nth-child(2) :nth-child(7) >button")
button.click()

#Создать пользователя
button1=browser.find_element_by_css_selector("//button[placeholder='Создать пользователя']")
button1.click()







