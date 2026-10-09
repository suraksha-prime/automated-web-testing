from database.db import save_test_result
from playwright.sync_api import sync_playwright
import time


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator("#user-name").fill("wrong_user")
        page.locator("#password").fill("wrong_password")
        page.locator("#login-button").click()

        error_message = page.locator("[data-test='error']")

        assert error_message.is_visible()
        save_test_result("Invalid Login Test", "PASS")

        print("Invalid login test passed!")

        time.sleep(5)

        browser.close()


test_invalid_login()