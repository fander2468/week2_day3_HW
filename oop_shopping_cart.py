
# Create a class called cart that retains items and has methods to add, remove, and show
class Cart():
    # Create an empty dictionary for future use.
    

    #class contructor 
    def __init__(self):
        self.my_cart = []
     
    # Create add function/method 
    def add(self, new_item):
        self.my_cart.append(new_item)

    # Create remove function/method 
    def remove(self, removed_item):
        print(self.show()) 
        removed_item = input("What would you like to remove:\n")
        self.my_cart.remove(removed_item)

    # Create show function/method
    def show(self):
        print("You have these items in your shopping cart:\n")
        for items in self.my_cart:
            print(items) 

    # Create clear function/method 
    def clear(self):
        self.my_cart.clear()
        print("You have emptied your cart.\n")


#run the program
def run_cart():
    print("Welcome to the shopping cart app")
    c = Cart()
    while True: 
        user_input = input("What would you like to do, 'Add', 'Remove', 'Show', 'Clear' or 'quit':\n")
        if user_input == 'add'.lower():
            user_input2 = input("What would you like to add:\n")
            c.add(user_input2)
        elif user_input == 'remove'.lower():
            c.remove(user_input2)
        elif user_input == 'show'.lower():
            c.show()
        elif user_input == 'clear'.lower():
            c.clear()
        elif user_input == 'quit'.lower():
            print('Thanks for shopping with us please come back again.\n')
            break
        else:
            print('Please only enter correct input, try agian.\n')
            continue

print(run_cart())