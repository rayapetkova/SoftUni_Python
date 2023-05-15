class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# Test code:

# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())
