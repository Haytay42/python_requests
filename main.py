from playwright.sync_api import Playwright, sync_playwright
import requests

with sync_playwright() as playwright:
    # Запускаем новый экземпляр браузера
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # Переходим на нужный URL
    page.goto("https://petstore.swagger.io/v2/pet/10")
    browser.close()
