from database.db import save_test_result
from playwright.sync_api import sync_playwright
import time


def test_remove_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        # Add product
        page.locator("#add-to-cart-sauce-labs-backpack").click()

        # Open cart
        page.locator(".shopping_cart_link").click()

        # Remove product
        page.locator("#remove-sauce-labs-backpack").click()

        # Verify product is removed
        product = page.locator(".inventory_item_name")

        assert not product.is_visible()
        save_test_result("Remove from Cart Test", "PASS")

        print("Remove from cart test passed!")

        time.sleep(5)

        browser.close()


test_remove_from_cart()