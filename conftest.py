import pytest
from selenium import webdriver
import webdriver_manager.chrome


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()