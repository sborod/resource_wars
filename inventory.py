class Inventory:
    def __init__(self, items={}):
        self.items = items

    def add_item(self, item_name, amount=1):
        if item_name in self.items:
            self.items[item_name] += amount
        else:
            self.items[item_name] = amount

    def remove_item(self, item_name, amount=1):
        if item_name not in self.items:
            return False

        if self.items[item_name] < amount:
            return False

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]

        return True

    def get_item_amount(self, item_name):
        if item_name not in self.items:
            return 0

        return self.items[item_name]
