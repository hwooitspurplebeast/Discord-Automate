from playwright.sync_api import sync_playwright

while True:
    user_input = input("Enter 'exit' to stop or press Enter to continue: ")
    if user_input.lower() == "exit":
        print("Exiting the program...")
        break
    
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    press_enter = input("Press Enter after login? (true/false): ").lower() == "true"
    screenshot_delay = int(input("Enter the time delay for taking screenshot (in seconds): "))
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto("https://discord.com/app")
        email_element = page.wait_for_selector('[name="email"]')
        email_element.type(email)
        password_element = page.query_selector('[name="password"], [name="Password"]')
        if password_element:
            password_element.type(password)
            if press_enter:
                password_element.press("Enter")
                page.wait_for_timeout(screenshot_delay * 1000)
                page.screenshot(path="screenshot.png")
                print("Screenshot taken.")
            else:
                page.wait_for_timeout(screenshot_delay * 1000)
                page.screenshot(path="screenshot.png")
                print("Screenshot taken.")
        else:
            print("Password element not found.")
        browser.close()
