class shopping_cart:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
    def __iter__(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item in self.items:
                print(f"- {item}")
    def __len__(self):
        return len(self.items)
    def __contains__(self,item):
        return item in self.items
    def __get_index__(self,item):
        if item not in self.items:
            print(f"{item} is not in your shopping cart.")
        else:
            print(f"{item} is in your shopping cart at {self.items.index(item)} position.")
    def __getitems__(self,index):
        if index < 0 or index >= len(self.items):
            print("Index out of range.")
        else:
            return self.items[index]
cart=shopping_cart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")
print(len(cart))
print(cart.__contains__("Banana"))
cart.__get_index__("Banana")
cart.__iter__()
