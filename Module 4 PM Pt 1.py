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

#inputs

item_num = int(input("Enter the number of items: "))
for i in range(item_num):
    name_input = input("Please enter item name: ")
    price_input = float(input("Please enter item price: "))
    quantity_input = int(input("Please enter item quantity: "))
    item = ItemToPurchase(name_input, price_input, quantity_input)
    item.print_item_cost()

