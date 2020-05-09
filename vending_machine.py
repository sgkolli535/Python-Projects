# Sumedha Kolli
# 9/15/2019
# Description:
# This is a program that calculates the amount of change from a vending machine with Harry Potter currency.
# The options are indented to make them easier to read.
item = input("Please select an item from the vending machine: "
             "\n    a) Butterbeer: 58 knuts "
             "\n    b) Quill: 10 knuts "
             "\n    c) The Daily Prophet: 7 knuts "
             "\n    d) Book of Spells: 400 knuts"
             "\n> ")

# all options are coded so that a capital or lower case letter will be taken.
# "it" is the variable used to put in the final print statement of what is bought.
# "price" is a variable that represents the price of the item. It is used to calculate change and is in the final print.
# the "ch" variable is the value in knuts of the price of the item chosen subtracted from 493 knuts, or 1 galleon.
# "ch" is an int variable, so that it can be involved in operations for determining change.
# "ch" is calculated by subtracting the integer "price" variable from the 493 knuts, or 1 galleon. used to pay.
if item == "a" or item == "A":
    it = "a Butterbeer"
    price = 58
    ch = 493 - price
elif item == "b" or item == "B":
    it = "a Quill"
    price = 10
    ch = 493 - price
# all the other options have an "a" before them, but this option has a "The", since it is a proper noun.
elif item == "c" or item == "C":
    it = "The Daily Prophet"
    price = 7
    ch = 493 - price
elif item == "d" or item == "D":
    it = "a Book of Spells"
    price = 400
    ch = 493 - price
# people that do not enter a valid option are automatically given a Butterbeer.
else:
    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
    it = "a Butterbeer"
    price = 58
    ch = 493 - price

# "insta" is the variable that takes into account the input of the question about sharing on Instagram.
insta = input("Will you share this on Instagram? (y/n): ")
# The insta variable takes into account inputs of lower and upper cases.
# change is a new variable that is used to take into account the discount of Instagram sharing.
# saying yes to insta sharing adds 5 knuts to the change given at the end to represent the discount.
# the "coupon" variable displays the actual discount of Instagram sharing in the final print statement.
if insta == "y" or insta == "Y":
    print("Thanks! You get 5 knuts off your purchase.")
    coupon = "(with coupon of 5 knuts)"
    change = ch + 5
# saying no to the insta sharing keeps the amount of change given at the end the same, with no coupon.
elif insta == "n" or insta == "N":
    coupon = "(with coupon of 0 knuts)"
    change = ch
# not entering a valid option automatically does not give a coupon.
else:
    print("You have entered an invalid option. No coupon will be used.")
    coupon = "(with coupon of 0 knuts)"
    change = ch

# sick change in sickles. Since 29 knuts is 1 sickle, integer division is used to determine a whole number.
sick = change // 29
# This operation is a modulus, because the remainder of change that cannot be a sickle becomes a knut.
knut = change % 29

# the "\n" is used to put a line of space between this statement and the previous one for easy readability.
# price is not shown as a string, since we need a space between the number and "knuts", which is given by a comma.
# "knuts" is the common label after price, since all of the items are only priced in knuts.
print("\nYou bought", it, "for", price, "knuts", coupon, "and paid with one galleon.")

# "change", "sick", and "knut2" are displayed as strings, because they are integers.
# the change is always given in knuts first, then shown in a combination of sickles and knuts.
print("Here is your change (" + str(change) + " knuts):")
print("Sickles: " + str(sick))
print("Knuts: " + str(knut))

