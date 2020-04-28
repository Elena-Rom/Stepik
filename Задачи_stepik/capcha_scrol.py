from selenium import webdriver
import calc as calc
import time
import math

host = "http://suninjuly.github.io/execute_script.html"
try:
    # Открыть браузер
    browser = webdriver.Chrome()
    browser.get(host)

    # Найти элемент
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text # Перевод найденного элемента в текст

    # Вычислить найденный элемент
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # Найти поле ввода и вписать найденное значение х
    vvod = browser.find_element_by_xpath('//input[@type="text"]')
    vvod.send_keys(y)

    #Проскролить страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")

    chec = browser.find_element_by_css_selector("[for='robotCheckbox']").click()# Выставить галочки на чекбоксе
    radio = browser.find_element_by_css_selector("[for='robotsRule']").click()# Выставить флажок на радио кнопке
    button = browser.find_element_by_class_name("btn-primary").click()# Нажать кнопку Submit
    #browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)

finally:
    time.sleep(10)
    browser.quit()