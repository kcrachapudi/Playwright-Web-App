class InventoryPage:

    def __init__(self, page):
        self.page = page

    inventory_container = ".inventory_list"

    def is_inventory_visible(self):
        return self.page.is_visible(self.inventory_container)