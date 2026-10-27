from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # для работы с ожиданиями
from selenium.webdriver.support import expected_conditions as EC # для работы с условиями
import time


def test_wikipedia_language_redirect(browser):
    # Главная страница, которая перенаправляет на ru.wikipedia, fr.wikipedia и т.д.
    browser.get("https://wikipedia.org")
    time.sleep(5) # смотрим сайт на том языке, который указали в консоли

    # Выводим адрес, на который нас в итоге перекинул сайт
    print(f"\n\n[INFO] Мы перешли на URL: {browser.current_url}\n")
