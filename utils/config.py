import os


class Config:

    # ============================
    # Environment Settings
    # ============================

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://www.saucedemo.com"
    )

    # Browser Settings
    HEADLESS = os.getenv(
        "HEADLESS",
        "true"
    ).lower() == "true"

    BROWSER = os.getenv(
        "BROWSER",
        "chromium"
    )