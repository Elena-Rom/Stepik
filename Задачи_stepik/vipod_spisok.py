from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти элементы
    num1_text = browser.find_element_by_id("num1")
    num2_text = browser.find_element_by_id("num2")
    # Переводим элементы в
    num1 = int(num1_text.text)
    num2 = int(num2_text.text)
    # Находим и выбираем из выпадающего списка сумму чисел
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num1+num2))  # ищем элемент(сторочку) с суммой чисел

    button = browser.find_element_by_class_name("btn-default").click()
finally:
    time.sleep(10)
    browser.quit()