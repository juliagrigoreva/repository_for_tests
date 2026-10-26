from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # для работы с ожиданиями
from selenium.webdriver.support import expected_conditions as EC # для работы с условиями

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_contains_an_add_to_cart_button(browser):
    browser.get(link)
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена!"
