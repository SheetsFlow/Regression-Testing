import re
from playwright.sync_api import Playwright, sync_playwright, expect
import os
import random
import string



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth_google.json")
    page = context.new_page()
    page.goto("https://docs.google.com/spreadsheets/d/1H5dWCnF5vMEEVtnoDxKtz4tTdEzQZvz7ybk1OwHom-U/edit?gid=839579597#gid=839579597")
    page.get_by_role("menuitem", name="Extensions").click()
    page.get_by_text("Clevervue►").click()
    page.get_by_text("Launch").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Import from...").click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.locator('//*[@id="index"]/div[2]/div[3]/div[2]/div[1]/button[2]').click()
    file_path = os.path.abspath("C:\\Users\\BTCCHL00037.BTCCHL0037\\PycharmProjects\\cross_browser_test_cv\\employees.csv")
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.locator("input[type='file'][accept='.csv']").set_input_files(file_path)

    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Import").click()
    page.get_by_role("dialog", name="Data preview").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Next", exact=True).click()
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("textbox", name="Workflow Name *").click()
    ran_d = ''.join(random.choices(string.ascii_lowercase, k=5))

    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("textbox", name="Workflow Name *").fill(ran_d)
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="Import").click()
    page.goto("https://docs.google.com/spreadsheets/d/1H5dWCnF5vMEEVtnoDxKtz4tTdEzQZvz7ybk1OwHom-U/edit?gid=1228314583#gid=1228314583")
    page.get_by_role("complementary", name="Clevervue").locator("iframe").content_frame.locator("#sandboxFrame").content_frame.locator("#userHtmlFrame").content_frame.get_by_role("button", name="home Go to Home").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
