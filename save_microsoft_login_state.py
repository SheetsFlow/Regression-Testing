from playwright.sync_api import sync_playwright

def save_login_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Go to your app
        page.goto("https://app.clevervue.ai/portal")

        # 2. Trigger Microsoft login (don’t try to track the popup)
        page.get_by_role("button", name="Microsoft Sign in with").click()

        print("\n🟢 Please complete Microsoft login manually (email, password, MFA if needed)...")

        # 3. Wait for a known element after successful login
        # Adjust selector below based on your app's dashboard
        page.get_by_role("button",name="Workflows Workflows").click()

        # 4. Save session state
        context.storage_state(path="auth.json")
        print("✅ Login completed! Saved to 'auth.json'.")

        browser.close()

if __name__ == "__main__":
    save_login_state()
