from selenium import webdriver
import calc as calc
import time
import math

host = "http://suninjuly.github.io/math.html"
try:

    browser = webdriver.Chrome()
    browser.get(host)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    vvod = browser.find_element_by_xpath('//input[@type="text"]')
    vvod.send_keys(y)

    chec = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radio=browser.find_element_by_css_selector("[for='robotsRule']").click()
    button=browser.find_element_by_xpath("//button [@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()