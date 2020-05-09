# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 3
# sgkolli@usc.edu
# This is a program that will print out the minimum, maximum, and average of a set of numbers entered by the user.
# The user is told to enter a positive number, or -1 to stop the program.
num = int(input("Input an integer greater than or equal to 0, or enter -1 to quit:\n> "))
# max is the variable that represents the largest number. When there is only one input, that number is the maximum.
max = num
# min is the variable that represents the smallest number. When there is only one input, that number is the minimum.
min = num
# sum is the variable for the sum of all the numbers. When there is only one input, that number is the sum.
sum = num
# numValues is the variable for the amount of numbers entered. With one number entered, numValues is 1.
numValues = 1
# The while loop is set so that the loop will continue as long as the number entered is not "-1".
while num != -1:
    # num takes on the value of every new number that is entered after the arrow.
    num = int(input("> "))
    # the new number entered is added to the existing sum of numbers, as long as it is not "-1".
    if num != -1:
        sum = sum + num
    # the new number entered allows for the set of numbers to increase by 1, as long as it is not "-1".
    if num != -1:
        numValues += 1
    # the new number entered is checked to see if it is less than the previous minimum, as long as it is not "-1".
    # if the new number is less than the previous minimum, it replaces the previous minimum.
    if num != -1 and num < min:
        min = num
    # the new number entered is checked to see if it is more than the previous maximum, as long as it is not "-1".
    # if the new number is more than the previous maximum, it replaces the previous maximum.
    if num != -1 and num > max:
        max = num
    # this if/else statement with a modulus is to determine if the sum is divisible by numValues with no remainders.
    # if the two are perfectly divisible, the avrg variable will be absolute division, with no decimal at the end.
    # if the two are not perfectly divisible, the avrg variable will be tru division, with a decimal for the remainder.
    if sum % numValues == 0:
        avrg = sum // numValues
    else:
        avrg = sum / numValues
print("The largest number is", max)
print("The smallest number is", min)
# the average number is calculated by the true division function of the sum variable by the numValues variable.
print("The average number is", avrg)

# After completing one sequence, the user is asked if they want to enter another set of numbers.
# the answer to this question, as either a "y" or "n" is stored in the choice variable.
choice = input("\nWould you like to enter another set of numbers? (y/n): ")
# the user is able to enter either a capital or lower-case "y" for yes.
# entering "y" or "Y" allows entrance into the while loop that will allow the user to enter another set of numbers.
while choice == "y" or choice == "Y":
    # the majority of the remaining code is repeated from the first sequence.
    # the main difference is that the user will be continuously asked if they want to go again once they finish.
    # the loop is broken when the user enters an input other than "y" or "Y".
    num = int(input("Input an integer greater than or equal to 0, or enter -1 to quit:\n> "))
    max = num
    min = num
    sum = num
    numValues = 1
    while num != -1:
        num = int(input("> "))
        if num != -1:
            sum = sum + num
        if num != -1:
            numValues += 1
        if num != -1 and num < min:
            min = num
        if num != -1 and num > max:
            max = num
        if sum % numValues == 0:
            avrg = sum // numValues
        else:
            avrg = sum / numValues
    print("The largest number is", max)
    print("The smallest number is", min)
    print("The average number is", avrg)
    # the user is continuously prompted this question after a sequence, because it is included in the while loop.
    choice = input("\nWould you like to enter another set of number? (y/n): ")
# when the user chooses not to enter another set of numbers, this greeting is displayed to signify the program's end.
print("\nGoodbye!")

