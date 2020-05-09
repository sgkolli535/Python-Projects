# Sumedha Kolli
# This program allows the user to play a game of "rock, paper, scissors" with the computer.
# the random module is imported to be used in a function later on.
import random

# this function is used to display the rules to the user.
# there are no inputs and the function does not return anything.
def displayMenu():
    # the function just prints out the rules of the games"
    # escape characters are used to make the menu easier to read.
    print("\nWelcome! Let's play rock, paper, scissors."
          "\nThe rules of the game are:"
          "\n\tRock smashes scissors"
          "\n\tScissors cut paper"
          "\n\tPaper covers rock"
          "\n\tIf both the choices are the same, it's a tie")

# this function uses the randint function for the values 0, 1, and 2 to generate a random computer choice.
# no inputs are needed.
def getComputerChoice():
    num = random.randint(0, 2)
    # this function returns a random integer that represents the computer's random choice.
    return num

# this function asks the user for their choice and takes their input to return the integer value of their choice.
# no inputs are needed.
def getPlayerChoice():
    # choice is the variable that takes the input of the option that the player chooses.
    choice = input("Please choose (0) for rock, (1) for paper or (2) for scissors\n")
    # while loop is used to tell the user to only enter one of the three valid options, if an invalid value is entered.
    while choice != "0" and choice != "1" and choice != "2":
        print("Please enter 0, 1, or 2.")
        choice = input("Please choose (0) for rock, (1) for paper or (2) for scissors\n")
    # the integer value that represents the choice of the user is returned.
    return int(choice)

# this function takes two parameters, the computer's choice and the player's choice.
def playRound(computerChoice, playerChoice):
    # 0 represents a tie, 1 represents a win for the player, and -1 represents a win for the computer.
    # for each if/elif statement an integer is returned that represents the outcome of the game based on the choices.
    if computerChoice == playerChoice:
        return 0
    elif computerChoice == 0 and playerChoice == 1:
        return 1
    elif computerChoice == 0 and playerChoice == 2:
        return -1
    elif computerChoice == 1 and playerChoice == 0:
        return -1
    elif computerChoice == 1 and playerChoice == 2:
        return 1
    elif computerChoice == 2 and playerChoice == 0:
        return 1
    elif computerChoice == 2 and playerChoice == 1:
        return -1

# this function is used to determine if the user wants to continue playing the game or not.
# no inputs are needed.
def continueGame():
    # cont is the variable that takes the input of whether the user wants to continue or not.
    cont = input("Do you want to continue playing? Enter (y) for yes or (n) for no.\n")
    # the user's input is converted to lower-case letter for easy comparability.
    cont = cont.lower()
    # if the user does not enter a valid input, they are asked to enter a valid input through this while loop.
    while cont != "y" and cont != "n":
        print("Please enter either (y) or (n).")
        cont = input("Do you want to continue playing? Enter (y) for yes or (n) for no.\n")
        cont = cont.lower()
    # if the user chooses to continue, then the boolean value of True is returned.
    if cont == "y":
        return True
    # if the user does not want to continue, then the boolean value of False is returned.
    else:
        return False

# this function is used to print out statements that show the interactions between different choices.
# the parameters are the computer's choice and the player's choice.
def getObject(num, num2):
    # num represents the computer's choice, and num2 represents the player's choice.
    # it does not matter who won; this function simply displays the interaction between the choices.
    # if both choices are a tie, no interaction needs to be printed.
    # depending on the computer's choice, then the player's choice, various strings are returned.
    if num == 0:
        if num2 == 1:
            return "Paper covers rock."
        elif num2 == 2:
            return "Rock smashes scissors."
    elif num == 1:
        if num2 == 0:
            return "Paper covers rock."
        elif num2 == 2:
            return "Scissors cut paper."
    elif num == 2:
        if num2 == 0:
            return "Rock smashes scissors."
        elif num2 == 1:
            return "Scissors cut paper."
    else:
        return "unknown"


# this function contains a while loop to call all the other functions until the user chooses to stop.
def main():
    # the following variable are used to determine how many games were tied, the player won, and the computer won.
    tie = 0
    win = 0
    lose = 0
    # cont is initially set to the boolean True, so that the while loop can execute for the first time.
    cont = True
    # the following while loop calls all of the other functions and executes until the function continueGame() is False.
    while cont:
        # the displayMenu() function is called to display the rules.
        displayMenu()
        # the getPlayerChoice() function is called, and the player's choice is stored in the variable pc.
        pc = getPlayerChoice()
        # the getComputerChoice() function is called, and the computer's choice is stored in the variable cc.
        cc = getComputerChoice()
        # the following if/elif statements print out what the user chose based on the integer they entered.
        if pc == 0:
            print("You chose rock.")
        elif pc == 1:
            print("You chose paper.")
        elif pc == 2:
            print("You chose scissors.")
        # the following if/elif statements print out what the computer chose based on the random integer generated.
        if cc == 0:
            print("The computer chose rock.")
        elif cc == 1:
            print("The computer chose paper.")
        elif cc == 2:
            print("The computer chose scissors.")
        # the following if/elif statements print out the outcome of the game based on calling the playRound() function.
        # the playRound() function is called with the parameters of getComputerChoice() and getPlayerChoice().
        # the playRound() function returns 0 for tie, 1 for player win, and -1 for computer win.
        if playRound(cc, pc) == 0:
            print("It's a tie!")
            # 1 is added to the counter for the number of tied games, when playRound() returns 0.
            tie += 1
        elif playRound(cc, pc) == 1:
            print(getObject(pc, cc), "You win!")
            # 1 is added to the counter for the number of player wins, when playRound() returns 1.
            win += 1
        elif playRound(cc, pc) == -1:
            print(getObject(cc, pc), "Computer wins!")
            # 1 is added to the counter for the number of computer wins, when playRound() returns -1.
            lose += 1
        # the initial booleanValue is equated to the continueGame() function that is called.
        # continueGame() will return a boolean value, and based on what it returns, the while loop will/will not be run.
        cont = continueGame()
    # if while loop does not run, the final results of the number of ties, computer wins, and player wins are printed.
    print("\nYou won", win, "game(s).")
    print("The computer won", lose, "game(s).")
    print("You tied with the computer", tie, "time(s).")


# the main function is called to call all the other functions and execute the program.
main()
