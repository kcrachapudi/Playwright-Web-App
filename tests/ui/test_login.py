from pages.login_page import LoginPage
from utils.config_loader import load_config

def test_login_ui(browser):
    config = load_config()
    browser.goto(config['base_url'] + "/login")
    login_page = LoginPage(browser)
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You Logged Into A Secure Area!" in browser.url
