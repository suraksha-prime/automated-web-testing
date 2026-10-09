from database.db import save_test_result
from playwright.sync_api import sync_playwright
import time


def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        # Add product to cart
        page.locator("#add-to-cart-sauce-labs-backpack").click()

        # Open cart
        page.locator(".shopping_cart_link").click()

        # Verify product is in cart
        product = page.locator(".inventory_item_name")

        assert product.is_visible()
        assert product.inner_text() == "Sauce Labs Backpack"
        save_test_result("Add to Cart Test", "PASS")

        print("Add to cart test passed!")

        time.sleep(5)

        browser.close()


test_add_to_cart()