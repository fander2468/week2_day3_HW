# Your assignment for the weekend is to create a parking garage class to get more familiar with Object Oriented Programming(OOP).


# Your parking gargage class should have the following methods:
class Parking_Garage:

# You will need a few attributes as well:
# - tickets       -> list - eveytime this is given out a pakingSpaces is decreased
# - parkingSpaces -> list - this is predetermined and will decrease as spaces are taken up
# - currentTicket -> dictionary
    def __init__(self, tickets = list(range(101)), parking = list(range(101)), current_ticket = {"is_paided": False}):
        self.tickets = tickets
        self.parking = parking
        self.current_ticket = current_ticket

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
    def take_ticket(self):
            del self.tickets[-1]
            print(f"There are {self.tickets[-1]} tickets available.")
            del self.parking[-1]
            print(f"There are {self.parking[-1]} parking spaces available")
    


    
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
    def pay_for_parking(self):
        display = int(input("Please pay for your ticket. The amount is 15.00 dollars: "))
        if not display or display <= 14.99:
            print("Please enter a correct amount for a ticket. Each ticket is 15.00 dollars for 15 mins\n")
        elif display == 15 and (self.tickets[-1] > 0 and self.parking[-1] > 0):
            print("Your ticket has been paid. Your ticket allots you 15 mins in the garage.\n")
            self.current_ticket['is_paid'] = True
            print('The current ticket paid status is:', self.current_ticket['is_paid'])
            self.take_ticket() 
        elif display > 15:
            print(f"Your ticket has been paid. Your ticket allots you 15 mins in the garage. Please take your change of: {display - 15}\n")
            self.current_ticket['is_paid'] = True
            print('The current ticket paid status is:', self.current_ticket['is_paid'])
            self.take_ticket() 
        elif self.tickets[-1] == 0 or self.parking[-1] == 0:
            print("We are sorry but there are no more parking spaces available")
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)
    def leave_garage(self):
        if self.current_ticket['is_paided'] == True: 
            print("Thank You, have a nice day, please come back again.\n")
            self.parking[-1] += 1
            self.tickets[-1] += 1
        elif self.current_ticket['is_paided'] == False:
            display = int(input(" Your have no ticket. You must pay for your parking before you leave. The amount is 15.00 dollars: "))
            if not display or display <= 14.99:
                print("Please enter a correct amount for a ticket. Each ticket is 15.00\n")
            elif display == 15:
                print("Your ticket has been paid. Please pay for it next time before entry.\n")
                self.current_ticket['is_paid'] = True
                print('The current ticket paid status is:', self.current_ticket['is_paid'])
                self.parking += 1
                self.tickets += 1 
                print("Thank You, have a nice day, please come back again.\n")
            elif display > 15:
                print(f"Your ticket has been paid. Please pay for it next time before entry.Please take your change of: {display - 15}\n")
                self.current_ticket['is_paid'] = True
                print('The current ticket paid status is:', self.current_ticket['is_paid'])
                self.parking += 1
                self.tickets += 1 
                print("Thank You, have a nice day, please come back again.\n")


# NOTE: this is an individual project, but class brainstorming is encouraged if you'd like to bounce ideas off one another and work together.

# By the end of this project each student should be able to:
# - Explain and/or demostrate creating classes
# - Explain and/or demostrate creating class methods
# - Explain and/or demostrate class instantiation 


# When the project is completed, commit the final changes and submit the link to your Github repository.


def run_parking_garage(car_approached):
    we_will_tow_it = Parking_Garage()
    if car_approached == 'entry': # check if car came through the entry way
        print("Welcome to the We Will Tow It parking garage\n")
        we_will_tow_it.pay_for_parking()
    elif car_approached == 'exit': # check if car came through the exit way
         print("Please scan your ticket before you leave.\n")
         we_will_tow_it.leave_garage()
  

while True:
    scan_car = input("Enter entry, exit or q to quit\n")
    if scan_car == 'entry': 
        run_parking_garage("entry".lower())
    elif scan_car == "exit":
        run_parking_garage("exit".lower())
    elif scan_car == "q".lower():
        break

