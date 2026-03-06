import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config


# ============================
# UI Fixture
# ============================
@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=Config.HEADLESS
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()


# ============================
# API Fixture
# ============================
@pytest.fixture(scope="session")
def api_request(playwright):

    request_context = playwright.request.new_context(
        base_url=Config.BASE_URL
    )

    yield request_context

    request_context.dispose()