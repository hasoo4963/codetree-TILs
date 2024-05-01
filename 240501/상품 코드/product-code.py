class Item:
    def __init__(self, item_name = "codetree", item_number=  "50"):
        self.item_name = item_name
        self.item_number = item_number
    def print(self):
        print(f"product {self.item_number} is {self.item_name}")

item = Item()
item.print()

item_name, item_number = tuple(map(str, input().split()))
item.item_name = item_name
item.item_number = int(item_number)
item.print()