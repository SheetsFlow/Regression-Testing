from playwright.sync_api import sync_playwright

def save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Go to your app
        page.goto(" https://docs.google.com/spreadsheets/d/1H5dWCnF5vMEEVtnoDxKtz4tTdEzQZvz7ybk1OwHom-U/edit?gid=839579597#gid=839579597")

        # 2. Trigger Microsoft login (don’t try to track the popup)
        page.get_by_role("textbox", name="Email or phone").fill("qc@clevervue.ai")

        
        page.get_by_role("menuitem", name="Launch", exact=True).locator("div").click()

        context.storage_state(path="auth_google.json")
        print("✅ Login completed! Saved to 'auth.json'.")

        browser.close()

if __name__ == "__main__":
    save_login_state()
