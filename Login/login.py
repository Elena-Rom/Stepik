from selenium import webdriver
import time

#host = "beta.hi-tech.org"
#login="admin@ivcs.su"
#password="test"

try:
    browser = webdriver.Chrome()
    browser.get("beta.hi-tech.org")
    input1 = browser.find_element_by_xpath('//input[@type="text"]')
    input1.send_keys("admin@ivcs.su")
    input2 = browser.find_element_by_xpath("//input[@type='password']")
    input2.send_keys("test")
    #input1 = browser.find_element_by_xpath('//input[@type="text"]').clear()

    button = browser.find_element_by_xpath("//div[@class='ivcs-button-text']")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
