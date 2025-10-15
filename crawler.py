from playwright.sync_api import sync_playwright, Playwright

def run(playwright):
    start_url = input("Please type start url: ")
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)
    base=input("Please type base url: ")

    while True:
        for link in page.locator("a").all():
            p = browser.new_page(base_url=base)
            url = link.get_attribute("href")

            if url is not None:
                p.goto(url)
            else:
                p.close()
            
            p.close()

with sync_playwright() as playwright:
    run(playwright)

