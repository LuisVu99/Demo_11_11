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
        page.locator("#side-menu").get_by_text("Customer").click()
        page.get_by_text("New Customer").click()
        page.locator("#company").fill("Luis_company")
        page.locator("#vat").fill("12345")
        page.locator("#phonenumber").fill("098768812")
        page.locator("#website").fill("luis@example.com")
        page.get_by_role("button", name="Save", exact=True).click()
        expect(page.get_by_text("Customer2 added successfully")).to_be_visible()
        context.close()
        browser.close()
