# Module 4 Portfolio Milestone // Online Shopping Cart

#Step 1: Build ItemToPurchase Class
#class
class ItemToPurchase:
    #attributes, unnecessary to state these as they are defined in __init__?
    item_name = str
    item_price = float
    item_quantity = int

    #default constructor
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ $ {self.item_price} = ${self.item_quantity * self.item_price}")
        total = self.item_price * self.item_quantity
        return total

#Step 2: Prompt user for items and create two objects
print("Please enter item information for two items below ")
name_input1 = input("Please enter item 1 name: ")
price_input1 = float(input("Please enter item 1 price: "))
quantity_input1 = int(input("Please enter item 1 quantity: "))
name_input2 = input("Please enter item 2 name: ")
price_input2 = float(input("Please enter item 2 price: "))
quantity_input2 = int(input("Please enter item 2 quantity: "))
item1 = ItemToPurchase(name_input1, price_input1, quantity_input1)
item2 = ItemToPurchase(name_input2, price_input2, quantity_input2)

#Step 3: Add costs and output total cost
print("TOTAL COST")
cost1 = item1.print_item_cost()
cost2 = item2.print_item_cost()
print(f"Total: $ {cost1+cost2}")

#Attempt with a loop to get inputs
# items = []
# item_num = int(input("Enter the number of items: "))
# for i in range(item_num):
#     name_input = input("Please enter item name: ")
#     price_input = float(input("Please enter item price: "))
#     quantity_input = int(input("Please enter item quantity: "))
#     item = ItemToPurchase(name_input, price_input, quantity_input)
#     items.append(item)
# print(items[0])
# I can't figure out the looping on this one, need to try different approach...
