from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.navigate()
    login.login("standard_user", "secret_sauce")

    page.wait_for_url("**/inventory.html")

    assert inventory.is_inventory_visible()