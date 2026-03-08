#import nest_asyncio
#nest_asyncio.apply()

import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config

# ============================
# Core Playwright Engine
# ============================
@pytest.fixture(scope="session")
def playwright_engine(): # Renamed to avoid confusion with the import
    with sync_playwright() as p:
        yield p



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
def api_request(playwright_engine):
    # Use 'playwright_engine' (the fixture) to create the request context
    request_context = playwright_engine.request.new_context(
        base_url=Config.BASE_URL
    )

    yield request_context

    request_context.dispose()
