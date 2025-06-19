import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
import random
import string

    
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth_google.json")  # ← using saved session
    page = context.new_page()
    page.goto("https://docs.google.com/spreadsheets/d/1H5dWCnF5vMEEVtnoDxKtz4tTdEzQZvz7ybk1OwHom-U/edit?gid=839579597#gid=839579597")
    page.get_by_role("menuitem", name="Extensions").click()
    page.get_by_text("Clevervue►").click()

    page.get_by_role("menuitem", name="Launch", exact=True).locator("div").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Import from...").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Google Sheets™ Google Sheets™").click()
    dialog_locator = page.get_by_role("dialog", name="Choose Google Sheet")

    # Drill down through nested iframes
    outer_frame = dialog_locator.frame_locator("iframe").first
    sandbox_frame = outer_frame.frame_locator("#sandboxFrame")
    user_html_frame = sandbox_frame.frame_locator("#userHtmlFrame")
    picker_frame = user_html_frame.frame_locator("iframe[name]")

    # Click on the first document in Google Picker
    picker_frame.locator(".doclist-grid-doc-thumb-inset-border").first.click()

    # Click the "Select" button
    picker_frame.get_by_role("button", name="Select").click()
    ## page.get_by_role("dialog", name="Choose Google Sheet").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.locator("iframe[name=\"egfwr51ykzch\"]").content_frame.locator(".doclist-grid-doc-thumb-inset-border").first.click()
    ##page.get_by_role("dialog", name="Choose Google Sheet").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.locator("iframe[name=\"egfwr51ykzch\"]").content_frame.get_by_role("button", name="Select").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.locator("label").filter(has_text="employees").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Preview").click()
    page.get_by_role("dialog", name="Data preview").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Next", exact=True).click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("textbox", name="Workflow Name *").click()
    ran_d = ''.join(random.choices(string.ascii_lowercase, k=5))

    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("textbox", name="Workflow Name *").fill(ran_d)
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Import").click()
    page.wait_for_timeout(15)
    print("workflow passed")



with sync_playwright() as playwright:
    run(playwright)
    time.sleep(30)
