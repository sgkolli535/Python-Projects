# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 4, Part 2
# sgkolli@usc.edu
# This is part 2 of the assignment. This program will simulate a game of rolling a D20 die.
import random
print("PART 2 - D20 Dice Game\n")
# the initial score is set to 0.
score = 0
# this for loop is to run the program 10 times to represent 10 rounds of the game.
for i in range(10):
    # whichCase is the variable that represents which case the user is assigned randomly for that round.
    whichCase = random.randrange(1, 6, 1)
    # dice is the variable that represents which side the D20 lands on for that round.
    dice = random.randrange(1, 21, 1)
    # there is an if/elif statement for every all the cases, 1-5.
    if whichCase == 1:
        print("You are playing for CASE", whichCase)
        print("You will win for the following numbers: ")
        # wincase is the list that represents the winning numbers for that particular case.
        wincase = [1, 2, 3, 4, 5]
        # this for-range loop is to print out the winning numbers for that case.
        for num in range(1, 6, 1):
            print(num, end=" ")
        # this is an extra space between the list of numbers and the "now rolling" statement.
        print("\n")
        print("Now rolling...")
        print("You rolled a", dice, "!")
        # this if statement is to determine if the dice landed on a side that is represented in the winning numbers.
        if dice in wincase:
            print("You won 50 points!\n")
            # 50 points are added to the total score if the side lands on a winning number.
            score += 50
        else:
            # no points are added to the total score if the side does not land on a winning number.
            print("You didn't win :(\n")
    elif whichCase == 2:
        print("You are playing for CASE", whichCase)
        print("You will win for the following numbers: ")
        wincase = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        for num in range(1, 20, 2):
            print(num, end=" ")
        print("\n")
        print("Now rolling... ")
        print("You rolled a", dice, "!")
        if dice in wincase:
            print("You won 50 points!\n")
            score += 50
        else:
            print("You didn't win :(\n")
    elif whichCase == 3:
        print("You are playing for CASE", whichCase)
        print("You will win for the following numbers: ")
        wincase = [5, 6, 7, 8, 9, 10]
        for num in range(5, 11, 1):
            print(num, end=" ")
        print("\n")
        print("Now rolling... ")
        print("You rolled a", dice, "!")
        if dice in wincase:
            print("You won 50 points!\n")
            score += 50
        else:
            print("You didn't win :(\n")
    elif whichCase == 4:
        print("You are playing for CASE", whichCase)
        print("You will win for the following numbers: ")
        wincase = [10, 12, 14, 16, 18, 20]
        for num in range(10, 21, 2):
            print(num, end=" ")
        print("\n")
        print("Now rolling... ")
        print("You rolled a", dice, "!")
        if dice in wincase:
            print("You won 50 points!\n")
            score += 50
        else:
            print("You didn't win :(\n")
    elif whichCase == 5:
        print("You are playing for CASE", whichCase)
        print("You will win for the following numbers: ")
        wincase = [3, 6, 9, 12, 15, 18]
        for num in range(3, 19, 3):
            print(num, end=" ")
        print("\n")
        print("Now rolling... ")
        print("You rolled a", dice, "!")
        if dice in wincase:
            print("You won 50 points!\n")
            score += 50
        else:
            print("You didn't win :(\n")
# the total score of the 10 rounds is printed following the rounds. The user is thanked for playing the game.
print("Your total score is:", score)
print("Thank you!")






