# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String 
# print the string in upper case


class Strings():

    def __init__(self, some_string = ''):
        self.some_string = some_string

    # getter method
    def get_string(self):
        return self.some_string.upper()

    # setter method
    def set_string(self, new_string):
        
        self.some_string = new_string



while True:
    user_input = input("Enter your string 'q' to quit:")
    if user_input == 'q':
        break
    elif not user_input:
        print('Please enter some string') 
    else:
        run_string = Strings()
        run_string.set_string(user_input)
        print(run_string.get_string()) 

print("Thanks for your input")


