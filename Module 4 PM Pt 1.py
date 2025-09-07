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

print("Please enter item information below ")
name_input1 = input("Please enter item name: ")
price_input1 = float(input("Please enter item price: "))
quantity_input1 = int(input("Please enter item quantity: "))
name_input2 = input("Please enter item name: ")
price_input2 = float(input("Please enter item price: "))
quantity_input2 = int(input("Please enter item quantity: "))
item1 = ItemToPurchase(name_input1, price_input1, quantity_input1)
item2 = ItemToPurchase(name_input2, price_input2, quantity_input2)

item1.print_item_cost()
item2.print_item_cost()


#inputs
# items = []
# item_num = int(input("Enter the number of items: "))
# for i in range(item_num):
#     name_input = input("Please enter item name: ")
#     price_input = float(input("Please enter item price: "))
#     quantity_input = int(input("Please enter item quantity: "))
#     item = ItemToPurchase(name_input, price_input, quantity_input)
#     items.append(item)
# print(items[0])
# I can't figure out the looping on this one, need to try different approach
