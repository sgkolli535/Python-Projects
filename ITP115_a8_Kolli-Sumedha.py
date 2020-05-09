# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 8
# sgkolli@usc.edu
# this is a program that creates a two-player Tic Tac Toe game.
# the given program with two functions is imported to be used within this program.
import TicTacToeHelper

# this is an extra credit function.
# this function prints the board with dashes and lines between the numbers too look like an actual board.
# the input of the function is the list of numbers that represents the board.
# There is no value that is returned.
def printPrettyBoard(boardList):
    # a blank like is printed to include a space between the previous like.
    print()
    # the counter is used to be able to print out each new row of numbers with for loops.
    counter = 0
    # this for loop iterates through the range of 3 to print out 3 rows of numbers.
    for i in range(3):
        # this for loop iterates through the range of 3 to print out 3 columns of numbers.
        for j in range(3):
            # this for loop iterates through the range of 2 to print out lines between each column of numbers.
            if j in range(2):
                # 2 lines are printed out between the three columns.
                print(boardList[counter], end=" | ")
            else:
                # the last column is printed with a spaces, not a line.
                print(boardList[counter], end=" ")
            # 1 is added to the counter to be able to print new column/row of numbers.
            counter += 1
        # 2 horizontal lines are printed out between the 3 rows of numbers.
        if i in range(2):
            print()
            print("---------")
        # the last row of numbers does not have anything printed underneath.
        else:
            print()

# this function is used to determine if the user enters an invalid input that will be changed on the board.
# the inputs are the list of the board and the index value on the board that the player chooses.
# this function returns the Boolean of either True or False.
def isValidMove(boardList, spot):
    # the string of the input is checked to be a number or not.
    if spot.isdigit():
        # the integer of the input is checked to be in the range of the list of numbers in the board, 0-8.
        if int(spot) in range(0, 9):
            # the integer of the input is checked in the list of the board to see if it is already taken.
            if boardList[int(spot)] == "x" or boardList[int(spot)] == "o":
                # if the spot is already taken, the function returns False.
                return False
            # if the function is a number, is in the correct range, and is still open, the function returns True.
            else:
                return True
        # if the input is not in the range of the list of number in the board, then the function returns False.
        else:
            return False
    # if the input is not a number, then the function returns False.
    else:
        return False

# this function replaces the player's letter with the index value they choose on the board.
# inputs are the list of the board, the index the player chooses, and the letter of the player.
# there are no returned values.
def updateBoard(boardList, spot, playerLetter):
    # the index is converted to an integer, because the player enters a string, and the values in the boardList are int.
    boardList[int(spot)] = playerLetter

# this function creates the simulation of actually playing the Tic Tac Toe game.
# there are no inputs and returned values for this game.
def playGame():
    # this is the list of numbers that represents the board.
    boardList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # this is a counter that keeps track of the total number of moves made during the game.
    moves = 0
    # this Boolean is created to be able to enter the while loop that conducts the game.
    win = False
    # this value will be alternated between each player when their turn comes.
    player = True
    # this Boolean is used to determine whether or not the board should be printed after running the while loop again.
    brd = True
    # the while loop runs when win is not False, so when win is True.
    while not win:
        # if brd is True, then the board is printed.
        if brd:
            # this function is called with the input of the list of the board .
            printPrettyBoard(boardList)
        # it is player x's turn for all of the even turns, beginning with turn 0.
        # if the modulus does not return 0, then it is player o's turn.
        if moves % 2 == 0:
            player = "x"
        else:
            player = "o"
        # the player is asked to choose an index on the board.
        spot = input("Player " + player + " pick a spot: ")
        # this function is called with inputs of the list of the board and the index chosen on the board.
        # if the function retuns the Boolean of True, the following if statement occurs.
        if isValidMove(boardList, spot):
            # if the input is in the range 0-8, is a number, and is not already taken, then the move counter has +1.
            moves += 1
            # this function is called with inputs of the list of the board, the index chosen, and player's letter.
            # updates the index chosen with the player's letter.
            updateBoard(boardList, spot, player)
            # this Boolean is set to True to print out the updated board for the player's turn.
            brd = True
        # if the player enters an invalid input, the function returns False, and this else statement conducts.
        else:
            # this statement is printed to show that the input was invalid.
            print("Invalid move, please try again.")
            # the while statement is run again to ask the user to enter a valid input.
            # brd is set to False to not print the board again when entering the while loop again.
            brd = False
        # this function is called from the other program to check if the player's turn caused the game to end.
        # the inputs of the function are the list that represents the board and the integer of the move counter.
        cw = TicTacToeHelper.checkForWinner(boardList, moves)
        # if the function returns "x", then the game is said to be over and the winner is determined to be "x".
        if cw == "x":
            # final board is printed.
            printPrettyBoard(boardList)
            # blank line is printed.
            print()
            print("Game Over!\nPlayer x is the winner!")
            # win is changed to True, so the while statement does not run again and does not conduct the game again.
            win = True
        # if the function returns "o", then the game is said to be over and the winner is determined to be "o".
        elif cw == "o":
            # final board is printed.
            printPrettyBoard(boardList)
            # blank line is printed.
            print()
            print("Game Over!\nPlayer o is the winner!")
            # win is changed to True, so the while statement does not run again and does not conduct the game again.
            win = True
        # if the function returns "s", the game is said to be over and the game has resulted in a stalemate.
        # this is where the move counter is used to determine if the number of moves made is more than 8.
        elif cw == "s":
            # final board is printed.
            printPrettyBoard(boardList)
            # blank line is printed.
            print()
            print("Game Over!\nStalemate reached!")
            # win is changed to True, so the while statement does not run again and does not conduct the game again.
            win = True
        # the else statement occurs if the function returns "n" and the game has not yet ended.
        else:
            # win is kept as False to allow for the while loop to run again to keep playing the game.
            win = False

# this is the main function that will conduct all the other functions and determines if player wants to keep playing.
# there are no inputs and returned values.
def main():
    # the welcome statement is printed.
    print("Welcome to Tic Tac Toe!")
    # this function is called to let the player go through an initial game of Tic Tac Toe.
    playGame()
    # this Boolean Value is set to True in order to enter the while loop.
    pg = True
    # this while loop is used to determine whether or not the player wants another round after the game has ended.
    while pg:
        # the player is asked if they want to play another round.
        rnd = input("Would you like to play another round? (y/n): ")
        # if the user enters "y", then playGame() is called again and another game occurs.
        if rnd.lower() == 'y':
            playGame()
        # if the user enters "n", then the goodbye statement is printed.
        elif rnd.lower() == 'n':
            print("Goodbye!")
            # pg is changed to False so the while loop cannot be run again.
            pg = False
        # if the user does not enter "y" or "n", then they are told that it is an invalid input.
        # the while loop conducts again to ask the user to enter a valid input, because pg is not changed.
        else:
            print("Invalid choice.")

# the main function is called to call all the other functions and run the whole program.
main()

