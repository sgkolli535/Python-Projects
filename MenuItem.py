# Sumedha Kolli
# ITP 115, Fall 2019
# sgkolli@usc.edu
# Final Project
# MenuItem Class

# one of the two classes that will represent the menu.
# this class will represent a single item a diner can order from the menu.


class MenuItem:
    # the constructor defines 4 instance attributes.
    # the 4 parameters/instance attributes are the name, type, price, and description of the menu item.
    def __init__(self, name, ty, price, description):
        self.name = name
        self.type = ty
        self.price = price
        self.description = description

    # getter method that returns the name of the menu item
    def getName(self):
        return self.name

    # getter method that returns the type of the menu item
    def getType(self):
        return self.type

    # getter method that returns the price of the menu item
    def getPrice(self):
        return self.price

    # getter method that returns the description of the menu item
    def getDescription(self):
        return self.description

    # setter method that sets a new value to the name of the menu item
    def setName(self, nName):
        self.name = nName

    # setter method that sets a new value to the type of the menu item
    def setType(self, nType):
        self.type = nType

    # setter method that sets a new value to the price of the menu item
    def setPrice(self, nPrice):
        self.price = nPrice

    # setter method that sets a new value to the description of the menu item.
    def setDescription(self, nDesc):
        self.description = nDesc

    # method that constructs a method for each menu item using its name, type, price and description.
    # when MenuItem object is printed, this method is called.
    def __str__(self):
        message = self.name + "(" + self.type + "):" + " $" + str(self.price) + "\n\t" + self.description
        # returns the formatted message to be printed.
        return message

