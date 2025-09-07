# Module 4 Portfolio Milestone // Online Shopping Cart

# Step 1: Building ItemToPurchase class

#class
class ItemToPurchase:
    #attributes, these were originally separate, but are no longer needed
    #because of the default constructor

    #item_name = ""
    #item_price = 0.0
    #item_quantity = 0


    #default constructor
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ $ {self.item_price} = ${self.item_quantity * self.item_price}")

item1 = ItemToPurchase(item_name = "Bottled Water", item_price = 1, item_quantity = 10)
item1.print_item_cost()