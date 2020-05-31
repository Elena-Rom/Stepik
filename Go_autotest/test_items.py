from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_get_link(browser):
    browser.get(link)
    time.sleep(15)
    assert browser.find_element_by_css_selector("div > :nth-child(6) [type='submit']"), "Кнопка не найдена"

