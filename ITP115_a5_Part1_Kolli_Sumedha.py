# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 5, Part 1
# sgkolli@usc.edu
# This is part 1 of assignment 5, where the user will be able to play a world jumble game.
import random
# This is a list of 10 words to be randomly assigned and jumbled.
words = ["amazing", "brilliant", "character", "diagram", "excellent", "fantastic", "gory", "hallows", "igloo", "jump"]
# this function will determine which word the user is randomly assigned.
randomWord = random.choice(words)
# the random word is equated to the variable right for when the user guesses the right word.
right = randomWord
# the random word is converted to a list to have the letters jumbled.
randomList = list(randomWord)
# the ctr is set to 0 initially, and for every try, 1 is added to the counter to print the number of tries at the end.
ctr = 0
# the following for loop is to jumble the random word.
for i in range(len(randomWord)):
    # a random position is generated from the list of the random word as an integer.
    randPosition = random.randint(0, len(randomList) - 1)
    # the random position is stored as a temp variable.
    temp = randomList[i]
    # the corresponding letter to the random position is found.
    randomList[i] = randomList[randPosition]
    # the letter is changed to a different position.
    randomList[randPosition] = temp
# the jumbled word is joined together as a list.
jumbledWord = "".join(randomList)
print("The jumbled word is", jumbledWord)
guess = input("Please enter your guess: ")
# the user's input is taken only in lower case letter to match the elements of the list.
guess = guess.lower()
# the user begins the game with 100 points.
point = 100
# the following while loop is to determine whether or not the user's guess is correct.
# this section is for if the guess is not correct and does not match the "right" word.
while guess != right:
    # for every guess, whether it is right or wrong, an attempt is added to the attempt counter.
    ctr += 1
    print("Try again.")
    # the user is asked if they would like a hint every time they have an incorrect guess.
    hint = input("Would you like a hint (y/n)? ")
    if hint == "y":
        # if the user chooses to have a hint, their score drops by ten points.
        point -= 10
        # all 10 words are matched with a corresponding hint for if the user asks to have a hint.
        if right == "amazing":
            print("This word starts with an 'a' and ends with a 'g'. It means awe-inspiring")
        elif right == "brilliant":
            print("This is another word for great and starts with a 'b'.")
        elif right == "character":
            print("This is the term for the main objects that a story revolves around.")
        elif right == "diagram":
            print("This is a type of picture that maps out a concept.")
        elif right == "excellent":
            print("This is a word that means great and starts with an 'e'.")
        elif right == "fantastic":
            print("This word of encouragement starts with an 'f'.")
        elif right == "gory":
            print("A term used to describe something gross and scary.")
        elif right == "hallows":
            print("Harry Potter and the Deathly -------")
        elif right == "igloo":
            print("The term for where an eskimo lives.")
        elif right == "jump":
            print("A synonym of 'leap' that start with a 'j'.")
    # the user is asked to guess again, if they entered an incorrect guess.
    guess = input("Please enter your guess: ")
# the else statement is for if the user has a correct guess.
else:
    # the correct guess still adds an attempt to the counter.
    ctr += 1
    print("You got it!")
    # the number of tries and the number of remaining points out of the total possible points is printed at the end.
    if ctr == 1:
        # the singular form of "try" is printed if the user took only on attempt.
        print("It took you", ctr, "try.")
    else:
        # for more than one attempt, "tries" is printed out.
        print("It took you", ctr, "tries.")
    print("You had a total of", point, "out of 100 points.")
