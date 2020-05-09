# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 6
# sgkolli@usc.edu
# this program will represent an automated reservation system for an airline company.
# It is a menu where the user can choose the option they want to complete.
# there are a total of 10 available seats in the plane.
TOTAL_SEATS = 10
# the number of filled seats starts at 0.
numFilledSeats = 0
# choice is defined to be "0" to initially enter the while loop.
choice = "0"
# this variable allows the user to enter the while loop again after inputting a valid value after an invalid one.
choice2 = "0"
# the seatingChart is an list of the available seats on the plane.
seatingChart = []
# 10 blank string is added to the empty list with this for loop.
for i in range(10):
    seatingChart.append("")
# there are 4 available first class seats.
firstClass = 4
# there are 6 available economy class seats.
economyClass = 6
# as long as the user does not enter -1 to quit, the while loop will continue.
while choice != "-1":
    # if choice2 does not equal 0, this means that the user is trying to enter a valid choice after an invalid one.
    if choice2 != "0":
        # the valid choice is equated to the choice variable to carry throughout the if-statements.
        choice = choice2
        # choice2 is once again equated to 0 to take care of more invalid inputs in the future.
        choice2 = "0"
    # if choice2, does equal 0, this means that there were no invalid inputs, and the user is normally shown the menu.
    else:
        # the menu of options are displayed.
        print("\n1: Assign Seat")
        print("2: Print Seat Map")
        print("3: Print Boarding Pass")
        print("-1: Quit.")
        choice = input("\n> ")
        # choice 1 is for if the user wants to assign a name to a seat to reserve it.
    if choice == "1":
        name = input("Please enter your first name: ")
        # the names are converted to all lower-case to make comparing easier.
        name = name.lower()
        # the user is asked if they want a first class or economy class seat.
        seatClass = int(input("Type 1 for First Class or Type 2 for Economy. \n>"))
        # this if statement is for if the user chooses a first class seat.
        if seatClass == 1:
            # the first blank string that represents an empty seat in the list is found.
            if "" in seatingChart:
                # the index of the first empty seat is found.
                index = seatingChart.index("")
                # this if statement is conducted as long as there are first class seats available.
                if firstClass > 0:
                    # the first blank string in the first class range (1-4, or index: 0-3) is assigned the name.
                    seatingChart[index] = name
                    # there is one less available seat.
                    TOTAL_SEATS -= 1
                    # there is one more filled seat.
                    numFilledSeats += 1
                    # there is one less available first class seat.
                    firstClass -= 1
                # the else statement conducts if all of the first class seats are full, so firstClass <= 0.
                else:
                    # the user is asked if they would like to be in economy instead.
                    full = input("The first class section is full. Would you like to be placed in economy (y/n)? ")
                    # the if-statement conducts if the user answers "y".
                    if full == "y":
                        # the next empty string/seat, which will be in economy since first class is full, is taken.
                        seatingChart[index] = name
                        # there is one less available seat.
                        TOTAL_SEATS -= 1
                        # there is one more taken seat.
                        numFilledSeats += 1
                        # there is one less available economy class seat.
                        economyClass -= 1
                    # if the user does not want to be in economy class, the following statement is printed.
                    else:
                        print("Next flight leaves in 3 hours.")
        # this elif statement is for if the user chooses an economy class seat.
        elif seatClass == 2:
            # the first empty string/seat is found.
            if "" in seatingChart:
                # this if statement is conducted, as long as there are available economy class seats available.
                if economyClass > 0:
                    # this variable is to determine the index at which the next available economy seat is.
                    # since the economy seats occur from 5-10, the index is number of available seats minus 10.
                    # since the default number of spots is 6, the index of the first seat is 4, or seat 5.
                    economySpot = 10 - economyClass
                    # the name is assigned to the first available economy seat.
                    seatingChart[economySpot] = name
                    # there is one less available seat.
                    TOTAL_SEATS -= 1
                    # one more seat is filled.
                    numFilledSeats += 1
                    # there is one less available economy seat.
                    economyClass -= 1
                # this else statement occurs when economyClass <= 0, so no economy seats are available.
                else:
                    # the user is asked if they would like a first class seat instead.
                    full2 = input("The economy class section is full. Would you like to be placed in first class (y/n)? ")
                    # the index of the first available first class seat is found.
                    index2 = seatingChart.index("")
                    # if the user enters "y", then this if statement conducts.
                    if full2 == "y":
                        # the user's name is assigned to the first empty string, which is first empty first class seat.
                        seatingChart[index2] = name
                        # one less available seat.
                        TOTAL_SEATS -= 1
                        # one more filled seat.
                        numFilledSeats += 1
                        # one less first class seat.
                        firstClass -= 1
                    # if the user does not want a first class seat, the following statement is printed.
                    else:
                        print("Next flight leaves in 3 hours.")
        # this elif statement occurs when all the seats are filled and there are no available seats left.
        elif numFilledSeats == 10 and TOTAL_SEATS == 0:
            print("Next flight leaves in 3 hours.")
    # this elif statement occurs if the user chooses choice 2, printing seat map.
    elif choice == "2":
        # 40 asterisks are printed before and after the seat map is printed.
        print("*" * 40)
        # val will come to represent every seat as the for loop continues through the list.
        val = 0
        for x in seatingChart:
            # the following if statement is to print the empty seats.
            if x == "":
                # this variable finds the index of every empty seat/blank string.
                # because index only finds the first blank string, this index will keep finding the next one.
                valIn = (seatingChart.index(x, val))
                # one is added to the index of the empty string to signify the seat number.
                val = valIn + 1
                # if the index of the seat numbers is from 0-3, or seats 1-4, it is printed with first class.
                if valIn <= 3:
                    print("First Class Seat #" + str(val) + ": Empty")
                # if the index is not in the first class range, it is printed with economy class.
                else:
                    print("Economy Class Seat #" + str(val) + ": Empty")
            # this elif statement is to print the seats that are already assigned.
            elif x != "":
                # this variable is to find the of all the assigned seats and add 1 to signify the seat number.
                inOfSeat = seatingChart.index(x) + 1
                # this if statement is for if the index is from 0-3, or seats 1-4, it is printed with first class.
                if seatingChart.index(x) <= 3:
                    print("First Class Seat #" + str(inOfSeat) + ":", x)
                # if the index is not in the first class range, it is printed with economy class.
                else:
                    print("Economy Class Seat #" + str(inOfSeat) + ":", x)
        print("*" * 40)
    # this elif statement is for if the user chooses choice 3, printing boarding pass.
    elif choice == "3":
        # the user can get boarding pass from the seat number or the name.
        bPass = int(input("Type 1 to get Boarding Pass by seat number\nType 2 to get Boarding Pass by name\n> "))
        # this if statement is for if the user wants boarding pass from seat number.
        if bPass == 1:
            whatSeat = int(input("What is the seat number? "))
            # the index of the seat in the list is one less than the seat number.
            whatSeat = whatSeat - 1
            # the seat number must be in the range of seats on the plane.
            if whatSeat <= 9:
                # the value of the element at the given index in the list is found.
                seatName = seatingChart[whatSeat]
                # if the index in the list is of an empty, seat, then the user is told that the seat is empty.
                if seatName == "":
                    print("This seat is empty.")
                # if the index in the list is not empty, then the boarding pass is printed.
                else:
                    # the boarding pass is printed.
                    print("\n======= BOARDING PASS =======")
                    # if the index of the seat is 0-3, then a first class boarding pass is printed.
                    if whatSeat <= 3:
                        # the seat number is one more than the index of the desired element.
                        print("First Class Seat #:", whatSeat + 1)
                    # if the index is not in the first class range, "economy class" is printed.
                    else:
                        print("Economy Class Seat #:", whatSeat + 1)
                    # the name of the passenger in the desired seat is printed.
                    print("Passenger Name:", seatName)
                    print("=" * 29)
            # if the number is not in the range, this statement is printed.
            else:
                print("Invalid number--no boarding pass found")
        # if the user wants the boarding pass from the passenger's name, this elif statement is conducted.
        elif bPass == 2:
            # the passenger's name is taken.
            passName = input("Enter passenger name: ")
            # the name is converted to all lower-case.
            passName = passName.lower()
            # the seatNumber is assigned a value outside of range to determine if list actually has given name.
            seatNumber = 20
            for n in seatingChart:
                # the seatNumber variable is given the index of the element that has the desired name in list.
                if n == passName:
                    # the seat number is one greater than the index of the element.
                    seatNumber = seatingChart.index(n) + 1
            # the boarding pass is only printed if the name is found, and the variable is not the default 20.
            if seatNumber != 20:
                print("\n======= BOARDING PASS =======")
                # if the seatNumber is in the first class range of 1-4, then first class is printed.
                if seatNumber <= 4:
                    print("First Class Seat #:", seatNumber)
                # if the seatNumber is not in the first class range, then economy class is printed.
                else:
                    print("Economy Class Seat #:", seatNumber)
                print("Passenger Name: " + passName)
                print("=" * 29)
            # if seatName is still 20, this means that the name was not found in the list, so there is no boarding pass.
            else:
                print("No passenger with that information could be found.")
    # if the user enters -1, the program quits.
    elif choice == "-1":
        print("Have a nice day!")
    # if the user enters an invalid choice, they are continuously asked until they enter a valid choice.
    else:
        choice2 = input("Please enter choice: ")
