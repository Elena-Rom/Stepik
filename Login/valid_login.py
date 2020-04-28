from selenium import webdriver
import time

host = "<host>"
#login=""
password="<pass>"
try:
    browser = webdriver.Chrome()
    browser.get(host)
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys("e.romas")
    input2 = browser.find_element_by_xpath("//input[@type='password']")
    input2.send_keys(password)
    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()
    #assert input1 == "true", 'Passed'
    time.sleep(2)

    input1 = browser.find_element_by_xpath('//input[@type="text"]').clear()
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys("e.romashkova@")
    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()
    time.sleep(2)

    input1 = browser.find_element_by_xpath('//input[@type="text"]').clear()
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys("e.romashkova@hi-tech.")
    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()
    time.sleep(2)

    input1 = browser.find_element_by_xpath('//input[@type="text"]').clear()
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys(" e.romashkova@hi-tech.su")
    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()
    #time.sleep(4)

finally:
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()
