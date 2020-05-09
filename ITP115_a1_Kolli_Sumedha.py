# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 1
# sgkolli@usc.edu
# This is a program to create a Mad Libs story
# This mad libs story is called "A Day at the Beach"

# These are the inputs for the program.
# There are 5 strings, including noun, verb, adverb, onomatopoeia, and an adjective.
# There are 3 integers and 1 float.
int1 = int(input("Enter a number:"))
flt = float(input("Enter a number with a decimal:"))
st1 = input("Enter a type of food:")
int2 = int(input("Enter a second number:"))
int3 = int(input("Enter a third number:"))
st2 = input("Enter a verb ending in 'ing':")
st3 = input("Enter an adverb ending in 'ly':")
st4 = input("Enter an onomatopoeia:")
st5 = input("Enter an adjective:")
# This is the multiplication operation used in the story with two of the integers.
int4 = int2 * int3

# This is the premise of the story.
# At least ____ days a month, I like to go to the beach with my friends.
# The beach is ____ miles from my house.
# When we reach the beach, we always eat ____ at the local crab shack.
# Each ____ is ____ dollars, and I usually order ____. The total comes out to be ____ dollars.
# The best part of going to the beach is ____.
# We always walk around the beach so ____.
# There was a loud ____!, and we turned around to see a ____ whale leap out of the water.
# There is never a dull day at the beach!

# The inout order is: int, float, noun(food), int, int, multiply, noun(food) again, verb, adverb, onomatopoeia, adj.

# Printing the story with the proper formatting of having quotations around the user inputs.
print('At least \"' + str(int1) + '\" days a month, I like to go to the beach with my friends. The beach is \"' + str(flt) + '\" miles from my house. When we reach the beach, we always eat \"' + st1 + '\" at the local crab shack. Each of the \"' + st1 + '\" is \"' + str(int2) + '\" dollars, and I usually order \"' + str(int3) + '\". The total comes out to be \"' + str(int4) + '\" dollars. The best part of going to the beach is \"' + st2 + '\". We always walk around the beach so \"' + st3 + '\". There was a loud \"' + st4 + '!\", and we turned around to see a \"' + st5 + '\" whale leap out of the water. There is never a dull day at the beach!')
