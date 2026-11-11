from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://crm.anhtester.com/admin/authentication")
        page.get_by_role("textbox", name="email").fill("admin@example.com")
        page.get_by_role("textbox", name="password").fill("123456")
        page.get_by_role("button", name="login").click()
        # logo = page.locator("#logo")
        expect(page.locator("#logo")).to_be_visible()
        context.close()
        browser.close()
        page.pause()
