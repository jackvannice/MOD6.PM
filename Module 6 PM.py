# Module 4 Portfolio Milestone // Online Shopping Cart

#Step 1: Build ItemToPurchase Class
#class
class ItemToPurchase:

    #default constructor
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = ""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    #method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
        total = self.item_price * self.item_quantity
        return total
'''
#Step 2: Prompt user for items and create two objects
print("Please enter item information for two items below ")
name_input1 = input("Please enter item 1 name: ")
price_input1 = float(input("Please enter item 1 price: "))
quantity_input1 = int(input("Please enter item 1 quantity: "))
desc_input1 = str(input("Please enter item 1 description: "))
name_input2 = input("Please enter item 2 name: ")
price_input2 = float(input("Please enter item 2 price: "))
quantity_input2 = int(input("Please enter item 2 quantity: "))
desc_input2 = str(input("Please enter item 2 description: "))
item1 = ItemToPurchase(name_input1, price_input1, quantity_input1, desc_input1)
item2 = ItemToPurchase(name_input2, price_input2, quantity_input2, desc_input2)
'''
#Step 3: Add costs and output total cost
#print("TOTAL COST")
#cost1 = item1.print_item_cost()
#cost2 = item2.print_item_cost()
#print(f"Total: ${cost1+cost2}")

#Step 4: create ShoppingCart Class

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_price != 0:
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_quantity * item.item_price)
        return total_cost
    def print_total(self):
        if len(self.cart_items) == 0:
            print("Shopping cart is empty.")
            return
        print(f"{self.customer_name}'s shopping cart - {self.current_date}")
        print(f"Number of items: {self.get_num_items_in_cart()}")

        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("Shopping cart is empty.")
            return
        print(f"{self.customer_name}'s shopping cart - {self.current_date}")
        print('Item descriptions: ')
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
'''
my_shopping_cart = ShoppingCart("John" , "February 1, 2020")

my_shopping_cart.add_item(item1)
my_shopping_cart.add_item(item2)

my_shopping_cart.print_total()
my_shopping_cart.print_descriptions()
'''

def print_menu(my_shopping_cart):
    while True:
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output item descriptions')
        print('o - Output shopping cart')
        print('q - Quit')

        user_choice = input("Please enter your choice: ").lower()
        if user_choice == 'a':
            print('Add item to cart')
            name = input("Please enter item name: \n")
            price = float(input("Please enter item price: \n"))
            quantity = int(input("Please enter item quantity: \n"))
            description = input("Please enter item description: \n")

            added_item = ItemToPurchase(name, price, quantity, description)
            my_shopping_cart.add_item(added_item)
        elif user_choice == 'r':
            print('Remove item from cart')
            name = input("Please enter item to remove: \n")
            my_shopping_cart.remove_item(name)
        elif user_choice == 'c':
            print('Change item quantity')
            name = input("Please enter item to change: \n")
            updated_quantity = int(input("Please enter updated item quantity: \n"))
            modified_item = ItemToPurchase(name, 0.0, updated_quantity)
            my_shopping_cart.modify_item(modified_item)
        elif user_choice == 'i':
            my_shopping_cart.print_descriptions()
        elif user_choice == 'o':
            my_shopping_cart.print_total()
        elif user_choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")
def main():
    customer_name = input("Please enter customer's name: ")
    current_date = input("Please enter current date: ")
    print(f"Customer name: {customer_name}")
    print(f"Current date: {current_date}")

    my_shopping_cart = ShoppingCart(customer_name, current_date)

    print_menu(my_shopping_cart)

if __name__ == '__main__':
    main()


