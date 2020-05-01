from selenium import webdriver
import time
import math
#import calc as calc

link="http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    cartinka = browser.find_element_by_id("treasure")
    x_value = cartinka.get_attribute ("valuex")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    #print(x_value)
    y = calc(x_value)

    vvod = browser.find_element_by_id('answer')
    vvod.send_keys(y)

    chec=browser.find_element_by_id("robotCheckbox").click()
    radio=browser.find_element_by_id("robotsRule").click()
    button=browser.find_element_by_xpath("//button [@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

