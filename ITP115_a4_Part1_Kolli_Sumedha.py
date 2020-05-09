# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 4, Part 1
# sgkolli@usc.edu
# This is part 1 of the assignment. This program will count the number of characters evident in the user's input.
print("PART 1 - Character Counter")
# sentence is the variable that represents the user's input that will have its characters counted.
sentence = input("Please enter a sentence: ")
# alphabet is the list that has all of the letters, including spaces and special characters.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"
            , "w", "x", "y", "z", " ", "Special Character"]
# count is the list that represents the placeholders for each of the letters, spaces, and special characters.
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ch stands for character in the sentence.
for ch in sentence:
    foundLetter = False
    # letterLocation is the location of the letter in the range of the alphabet list.
    for letterLocation in range(len(alphabet)):
        # if the character is found in the alphabet, foundLetter is marked as true.
        if ch == alphabet[letterLocation]:
            foundLetter = True
            # for the count of that particular character, a counter of 1 is added to that character's location.
            count[letterLocation] += 1
    # if the character is neither a letter or space, it is counted as a special character at this location.
    if not foundLetter:
        count[27] += 1
# This for loop is to change the 0 value to NONE.
# n is the position of the 0 in the list. i is the how many times each 0 at a position has occurred.
# the enumerate function is to change every character that has 0 appearances to have "NONE" next to it.
for n, i in enumerate(count):
    if i == 0:
        count[n] = "NONE"
    else:
        count[n] = (i * "*")
# This for loop is to display the lists side by side.
# the variable a represents the alphabet list, and the variable c represents the count list.
# the zip function brings the two lists to be displayed side by side.
for a, c in zip(alphabet, count):
    print(a + ":" + "\t" + str(c))


