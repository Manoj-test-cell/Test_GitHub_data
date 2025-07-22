from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.fixture(scope="session") 
def test_browser():
    with sync_playwright as p:
        browser = p.chromium.launch()
        print("in browser")
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = browser.new_page()
    yield page
    page.close()  







