from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    # Присвоить имя для второй вкладки
    new_window = browser.window_handles[1]
    # Перейти на вторую вкладку
    browser.switch_to.window(new_window)
    #first_window = browser.window_handles[0] # Сохранить текущую вкладку

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    vvod = browser.find_element_by_xpath('//input[@type="text"]')
    vvod.send_keys(y)

    button=browser.find_element_by_xpath("//button [@type='submit']").click()
    #browser.switch_to.window(first_window)
finally:
    time.sleep(10)
    browser.quit()