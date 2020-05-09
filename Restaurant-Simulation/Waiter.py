# Sumedha Kolli
# Waiter Class

# import statements to use Diner and Menu objects
from Diner import Diner
from Menu import Menu


# class that represents the waiter, who continues through the list of diners and progresses through their statuses.
class Waiter:
    # constructor method has one input, a Menu object
    def __init__(self, menu):
        # the two instance attributes defined in the constructor are a Menu object and a list of Diner objects.
        self.menu = menu
        self.diners = []

    # method that adds a new diner to the waiter's list of diners.
    # input is a Diner object
    def addDiner(self, diner):
        # a new Diner object is added to the list of diners.
        self.diners.append(diner)

    # method that returns the number of diners that the waiter is keeping track of.
    # no additional inputs required
    def getNumDiners(self):
        # returns an integer of the length of the list of Diner objects in self.diners
        return len(self.diners)

    # method that prints the current diners categorized by their statuses.
    # no additional inputs required
    def printDinerStatuses(self):
        # a range-based for loop from 0 to 5 is used to run the code for the total number of possible diner statuses.
        # every iteration is for a different status.
        for x in range(0, 5):
            # empty list is initialized that will add the diners when they are a particular status.
            aList = []
            # for loop is used to iterate through the list of Diner objects.
            for i in self.diners:
                # if statement used to determine if diner is of particular status by calling Diner class variable list.
                # getter method is called on Diner object to determine the status
                if i.getStatus() == Diner.STATUSES[x]:
                    # if Diner object has particular status, then they are appended to the empty list.
                    aList.append(i)
            # the header is printed to specify which diners have that particular status.
            # the class variable in Diner is called at the index x from the initial range-based for loop.
            print("Diners who are " + Diner.STATUSES[x] + ":")
            # the diners that are determined to be of a particular status are printed by iterating through aList.
            for j in aList:
                print(j)

    # method that loops through list of diners to check if they are ordering. Menu's are printed and orders are taken.
    # diner's total order is printed after all of the orders are taken.
    # no additional inputs are required.
    def takeOrders(self):
        # the list of Diner objects is iterated through using a for loop
        for i in self.diners:
            # the getter method from the Diner class is used to retrieve the status of the Diner object.
            if i.getStatus() == "ordering":
                # range-based for loop used to iterate through the different types of menu items.
                # the length of the list of the class variable in Menu with the types of menu items is the max range.
                for j in range(0, len(self.menu.MENU_ITEM_TYPES)):
                    # value at index j in class variable from the Menu class is called and defined as the variable k.
                    k = self.menu.MENU_ITEM_TYPES[j]
                    # printMenuItemsByType is called on Menu object within list of self.menu
                    # the menu is printed depending on the type
                    self.menu.printMenuItemsByType(k)
                    # getter method for name of diner in list of Diner objects is called.
                    # message is printed asking diner to input a menu item number that represents their order.
                    item = input(i.getName() + ", please select a " + k + " menu item number. \n> ")
                    # error checking is used to make sure that user enters a valid input.
                    # the user's input is checked to be a number or not.
                    while not item.isdigit():
                        # if the user's input is not a number, then they are prompted to enter another input.
                        item = input("> ")
                    # user's input is checked to be length of 1, because they can only order one item of each menu type.
                    while len(item) != 1:
                        # if input is greater than length 1, then user is prompted to enter another input.
                        item = input("> ")
                    # user's number is checked to be in range of the menu item choices.
                    # this is checked by the input being in a range from 0 to the number of menu items in that type.
                    while int(item) not in range(0, self.menu.getNumMenuItemsByType(k)):
                        # user is asked to enter another input if choice is not in range of available items.
                        item = input("> ")
                    # once passing error checking, the user's order is added to the diner's total order.
                    # the number entered is correlated with the index of the menu item within the list of Menu objects.
                    # this is done by calling the addToOrder method from the Diner method on the Diner object.
                    i.addToOrder(self.menu.getMenuItem(k, int(item)))
                # the all of the diner's orders are printed after they ordered one of each menu item type.
                i.printOrder()

    # checks for diner's status to be "paying" and prints message with meal cost.
    # no additional inputs are required.
    def ringUpDiners(self):
        # iterate through list of Diner objects using for loop.
        for i in self.diners:
            # getter method for status of diner from Diner class is called to check if status is "paying".
            if i.getStatus() == "paying":
                # calculateMealCost method from Diner class is called to total the costs of all menu items ordered.
                cost = i.calcualteMealCost()
                # getter for diner's name is called to be in message that tells diner how much their total meal costs.
                print("\n" + i.getName() + ", your meal cost $" + str(cost))

    # removes the finished diners from the list when their status is "leaving".
    # no additional inputs are required
    def removeDoneDiners(self):
        # range based for loop that will iterate through the list of diners backwards.
        # the getNumDiners within the Waiter class is called to make the range possible, since it returns num of diners.
        for i in range(self.getNumDiners()-1, -1, -1):
            # getter for status of diner is called from the Diner class to check if the status is "leaving".
            if self.diners[i].getStatus() == "leaving":
                # getter for name of diner from Diner class is called to print a goodbye statement for leaving diner.
                print("\n" + self.diners[i].getName(), "thank you for dining with us! Come again soon!")
                # Diner object is deleted from list after leaving.
                del self.diners[i]

    # allows for the diner to attend to and advance each of the diners to the next stage.
    # no additional inputs are required.
    def advanceDiners(self):
        # calls the following four methods that were previously defined within the Waiter class
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        # iterate through the list of Diner objects using a for loop
        for i in self.diners:
            # calls the updateStatus method on the Diner object to change the diner's status.
            i.updateStatus()













