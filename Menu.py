# Sumedha Kolli
# ITP 115, Fall 2019
# sgkolli@usc.edu
# Final Project
# Menu Class

# because this class will use MenuItem objects, the MenuItem class from the MenuItem file is imported
from MenuItem import MenuItem


# this class as a whole will represent the four different types of menus from which the diner must choose their items.
class Menu:
    # this is a class variable that is a list of strings of the 4 types of menu items.
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # the constructor for this method is defined here.
    # the only parameter for the constructor is a string that represents the name of the csv file with the menu items.
    def __init__(self, fileName):
        # EXTRA CREDIT: a single dictionary is used instead of four lists.
        # a dictionary containing all of the menu items is defined.
        # 4 keys within the dictionary are defined as strings that represent the types of the menu items.
        self.menuItemDictionary = {"Drink": [], "Appetizer": [], "Entree": [], "Dessert": []}
        # the csv file is opened and read.
        fileIn = open(fileName, "r")
        # the csv file is iterated through using a for loop.
        for line in fileIn:
            # each line in the file is stripped of trailing white space and split using a comma to be made into a list.
            # each line represents a different menu item.
            # splitting line into a list allows for the different attributes of the menu item to be separated by index.
            aList = line.strip().split(",")
            # obj is the MenuItem object that contains the information from the indices of the list of each line.
            # index 0 is the name, index 1 is the type, index 2 is the price, and index 3 is the description.
            # the name, type, and description are set to strings. the price is set to a float.
            obj = MenuItem(str(aList[0]), str(aList[1]), float(aList[2]), str(aList[3]))
            # index 1 in aList represents the type of menu item it is.
            # if/elif statements determine what type of menu item each obj is by comparing to class variable's values.
            if aList[1] == Menu.MENU_ITEM_TYPES[0]:
                # if determined to be a drink, the obj is appended to the Drink key within the dictionary.
                self.menuItemDictionary["Drink"].append(obj)
            elif aList[1] == Menu.MENU_ITEM_TYPES[1]:
                # if determined to be an appetizer, the obj is appended to the Appetizer key within the dictionary.
                self.menuItemDictionary["Appetizer"].append(obj)
            elif aList[1] == Menu.MENU_ITEM_TYPES[2]:
                # if determined to be an entree, the obj is appended to the Entree key within the dictionary.
                self.menuItemDictionary["Entree"].append(obj)
            elif aList[1] == Menu.MENU_ITEM_TYPES[3]:
                # if determined to be a dessert, the obj is appended to the Dessert key within the dictionary.
                self.menuItemDictionary["Dessert"].append(obj)
        # the file is closed
        fileIn.close()

    # method to retrieve a specific menu item
    # parameters are a string that is the item type from the class variable, and an int that is index of the menu item.
    # returns the menu item at the specific index that was inputted.
    def getMenuItem(self, ty, num):
        # based on the type of the menu item, the specific key of the dictionary is called.
        if ty == Menu.MENU_ITEM_TYPES[0]:
            # ret = self.menuItemDictionary.get("Drink"[num])
            # if determined to be a drink, the Drink key is searched and the menu item is returned at specific index.
            return self.menuItemDictionary["Drink"][num]
        elif ty == Menu.MENU_ITEM_TYPES[1]:
            # ret = self.menuItemDictionary.get("Appetizer"[num])
            # if determined to be appetizer, Appetizer key is searched and the menu item is returned at specific index.
            return self.menuItemDictionary["Appetizer"][num]
        elif ty == Menu.MENU_ITEM_TYPES[2]:
            # ret = self.menuItemDictionary.get("Entree"[num])
            # if determined to be entree, the Entree key is searched and the menu item is returned at specific index.
            return self.menuItemDictionary["Entree"][num]
        elif ty == Menu.MENU_ITEM_TYPES[3]:
            # ret = self.menuItemDictionary.get("Dessert"[num])
            # if determined to be a dessert, Dessert key is searched and the menu item is returned at specific index.
            return self.menuItemDictionary["Dessert"][num]
        # return ret

    # method that iterates through each key in the dictionary and prints out the menu based on type in class variable.
    # parameter is string that represents the type of the menu item that is one of the 4 in the class variable.
    def printMenuItemsByType(self, ty):
        # counter is initialized to be 0.
        counter = 0
        # if the menu item type is determined to be a drink
        if ty == Menu.MENU_ITEM_TYPES[0]:
            # header is printed to identify what type of items are in the menu
            print("\n-----DRINKS-----")
            # the Drink key is iterated through using a for loop.
            for i in self.menuItemDictionary["Drink"]:
                # each item within the key is printed in a numbered list.
                print(str(counter) + ")", i)
                # 1 is added to the counter each time to be consistent as a numbered list.
                counter += 1
        # if the menu item type is determined to be an appetizer
        elif ty == Menu.MENU_ITEM_TYPES[1]:
            # header is printed to identify what type of items are in the menu
            print("\n-----APPETIZERS-----")
            # the Appetizer key is iterated through using a for loop.
            for i in self.menuItemDictionary["Appetizer"]:
                # each item within the key is printed in a numbered list.
                print(str(counter) + ")", i)
                # 1 is added to the counter each time to be consistent as a numbered list.
                counter += 1
        # if the menu item type is determined to be an entree
        elif ty == Menu.MENU_ITEM_TYPES[2]:
            # header is printed to identify what type of items are in the menu
            print("\n-----ENTREES-----")
            # the Entree key is iterated through using a for loop.
            for i in self.menuItemDictionary["Entree"]:
                # each item within the key is printed in a numbered list.
                print(str(counter) + ")", i)
                # 1 is added to the counter each time to be consistent as a numbered list.
                counter += 1
        # if the menu item type is determined to be a dessert
        elif ty == Menu.MENU_ITEM_TYPES[3]:
            # header is printed to identify what type of items are in the menu
            print("\n-----DESSERTS-----")
            # the Dessert key is iterated through using a for loop.
            for i in self.menuItemDictionary["Dessert"]:
                # each item within the key is printed in a numbered list.
                print(str(counter) + ")", i)
                # 1 is added to the counter each time to be consistent as a numbered list.
                counter += 1

    # method that returns the number of menu items of each type.
    # parameter is a string of menu item type that is one of 4 in the class variable.
    def getNumMenuItemsByType(self, ty):
        # if menu item type is a drink
        if ty == Menu.MENU_ITEM_TYPES[0]:
            # integer that represents the length of the Drink key in dictionary is returned
            return len(self.menuItemDictionary["Drink"])
        # if menu item type is an appetizer
        elif ty == Menu.MENU_ITEM_TYPES[1]:
            # integer that represents the length of the Appetizer key in dictionary is returned
            return len(self.menuItemDictionary["Appetizer"])
        # if menu item type is an entree
        elif ty == Menu.MENU_ITEM_TYPES[2]:
            # integer that represents the length of the Entree key in dictionary is returned
            return len(self.menuItemDictionary["Entree"])
        # if menu item type is a dessert
        elif ty == Menu.MENU_ITEM_TYPES[3]:
            # integer that represents the length of the Dessert key in dictionary is returned
            return len(self.menuItemDictionary["Dessert"])



