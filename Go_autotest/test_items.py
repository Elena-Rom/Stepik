from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_get_link(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("div > :nth-child(6) [type='submit']")
    butt_txt = button.text
    assert butt_txt, "Кнопка не найдена"
