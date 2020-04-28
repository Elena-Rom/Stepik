from selenium import webdriver
import time

host = "<stand>"
login="<login>"
password="<password>"

try:
    browser = webdriver.Chrome()
    browser.get(host)
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys(login)
    input2 = browser.find_element_by_xpath("//input[@type='password']")
    input2.send_keys(password)
    #input1 = browser.find_element_by_xpath('//input[@type="text"]').clear()

    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
