from  selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn-primary").click()
    time.sleep(2)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    vvod = browser.find_element_by_xpath('//input[@type="text"]')
    vvod.send_keys(y)

    button=browser.find_element_by_xpath("//button [@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()