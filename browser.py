# open_browser.py
import playwright

def main():
    # Initialize the browser
    browser = playwright.chromium.launch(headless=False)

    # Open a new page
    page = browser.new_page()

    # Navigate to a webpage
    page.goto("https://www.example.com")

    # Wait for a specific element to load
    page.wait_for_selector("#content")

    # Close the browser
    browser.close()

if __name__ == "__main__":
    main()
