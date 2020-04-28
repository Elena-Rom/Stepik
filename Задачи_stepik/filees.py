from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    #Открыть браузер
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполнить текстовые поля: имя, фамилия, email
    name_first = browser.find_element_by_css_selector("input[placeholder=\"Enter first name\"]")
    name_first.send_keys("Anna")
    name_last = browser.find_element_by_css_selector("input[placeholder=\"Enter last name\"]")
    name_last.send_keys("Rom")
    email = browser.find_element_by_css_selector("input[placeholder=\"Enter email\"]")
    email.send_keys("a.rom@gmail.com")

    file_button = browser.find_element_by_xpath("//input[@type='file']")# Найти элемент "Выберите файл"
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')        # добавляем к этому пути имя файла
    file_button.send_keys(file_path) #Добаввляем файл "file.txt"

    button = browser.find_element_by_class_name("btn-primary").click()

finally:

    time.sleep(10)
    browser.quit()






