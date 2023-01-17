from pages.base_page import BasePage

def test_elements(browser):
    page = BasePage(browser, "https://www.google.com/")
    page.open()
