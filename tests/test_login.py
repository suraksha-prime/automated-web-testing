from database.db import save_test_result
from playwright.sync_api import sync_playwright
import time


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        assert page.url == "https://www.saucedemo.com/inventory.html"
        save_test_result("Login Test", "PASS")

        print("Login test passed!")

        time.sleep(5)

        browser.close()


test_login_success()