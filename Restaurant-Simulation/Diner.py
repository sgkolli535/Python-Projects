# Sumedha Kolli
# Diner Class

# import statement to use MenuItem objects
from MenuItem import MenuItem


# Diner class that will represent a diner's status and meal within the restaurant
class Diner:
    # class variable that is a list of strings of the different types of statuses that a diner could have.
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    # the constructor defines three instance attributes.
    # the parameter is a string that represents the diner's name.

    def __init__(self, name):
        # the first instance attribute is a string of the diner's name
        self.name = name
        # the second instance attribute is a list of the diner's ordered MenuItem objects.
        self.order = []
        # the third instance attribute is an integer that represents the diner's status.
        # initialized to be 0 when the diner first enters restaurant.
        self.status = 0

    # getter method that returns a string of the diner'a name
    def getName(self):
        return self.name

    # getter method that returns the list of the diner's MenuItem orders
    def getOrder(self):
        return self.order

    # getter method that returns the status of the diner based on using the integer as the index in class variable.
    def getStatus(self):
        return Diner.STATUSES[self.status]

    # setter method that sets a new value to the name instance attribute.
    def setName(self, nName):
        self.name = nName

    # setter method that sets a new value to the order instance attribute.
    def setOrder(self, nOrder):
        self.order = nOrder

    # setter method that sets a new value to the status instance attribute.
    def setStatus(self, nStatus):
        self.status = nStatus

    # method that changes the diner's status
    # no additional inputs required
    def updateStatus(self):
        # increased the diner's status by one to represent their status changing
        self.status += 1

    # method that adds a MenuItem object to the diner's order
    # parameter is a MenuItem object
    def addToOrder(self, obj):
        # the MenuItem object is added to the diner's total order
        self.order.append(obj)

    # method that prints a message of all the menu items the diner ordered.
    # no additional inputs required
    def printOrder(self):
        # print the diner's name as part of the header to print message of their total order.
        print("\n" + self.name + " ordered:")
        # the list of the diner's order is iterated through using a for loop.
        for i in self.order:
            # if i is not None:
            # each menu item within the list is printed.
            print("-", i)

    # method that calculates the total cost of all of the diner's orders
    # no additional inputs are required
    def calcualteMealCost(self):
        # the total is initialized to be 0.
        total = 0
        # the list of the items that the diner ordered is iterated through using a for loop.
        for i in self.order:
            # get price of each item by calling the getPrice method from the MenuItem class on the MenuItem object
            # the float prices of each item are added to create the total.
            total += float(i.getPrice())
        # a float that represents the total cost of the diner's meal is returned.
        return total

    # method that is called when the message is printed
    # creates a message that has the diner's name and their current status.
    # no additional inputs are required
    def __str__(self):
        # the message is created containing the diner's name and current status.
        message = "\tDiner " + self.name + " is currently " + self.getStatus() + "."
        # the message is returned.
        return message

