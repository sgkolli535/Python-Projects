# Sumedha Kolli
# this is a program that allows the user to store results from an EPA Mileage Calculator.

# this function will open, read the file, add all the mileages to a list, and close the file.
# this function returns the list of mileages of the year chosen.
# the parameter is the file chosen by the user, either 2008 or 2009.
def readFile(fileName):
    # this list is used to store all the items in the file that are separated by a comma.
    dList = []
    # this list will contain all the mileages.
    aList = []
    # the file is opened and read.
    fileIn = open(fileName, "r")
    # the first row of the file is skipped and not read, since this row is just captions and does not have data.
    next(fileIn)
    # this for loop iterates through the whole file and adds the mileages to aList.
    for line in fileIn:
        # every line in the file is separated with a comma and is added to this list.
        dList = line.split(",")
        # this if statement excludes the data that follows a caption that is a van, minivan, or truck.
        # this format is used to make the code easier to read.
        # the index zero is the line that shows the type of vehicle for the following data.
        if dList[0] != "VANS - CARGO TYPE" \
                and dList[0] != "SMALL PICKUP TRUCKS 2WD" \
                and dList[0] != "STANDARD PICKUP TRUCKS 2WD" \
                and dList[0] != "VANS - PASSENGER TYPE" \
                and dList[0] != "MINIVAN - 2WD" \
                and dList[0] != "MINIVAN - 4WD" \
                and dList[0] != "STANDARD PICKUP TRUCKS 4WD" \
                and dList[0] != "SMALL PICKUP TRUCKS 4WD":
            # index 8 is the line with all of the mileages listed.
            # the mileages that are not from vans, minivans, or trucks are added to the aList.
            aList.append(int(dList[8]))
    # the file is closed.
    fileIn.close()
    # the list of mileages is returned.
    return aList

# this function will open and read the file, add all the vehicles with extreme mileages to a list, and close the file.
# this function will return a list with the vehicles that correspond to the extreme mileages.
# the parameters are the file chosen by the user, either 2008 or 2009, and the maximum or minimum mileages.
def readVal(fileName, num1):
    # dList will store the data as separated by commas.
    dList = []
    # nList will store the labels of the vehicles with extreme mileages.
    nList = []
    # val1 will represent the maximum and minimum mileages that will be searched for to find their vehicle types.
    val1 = num1

    # the file is opened and read.
    fileIn = open(fileName, "r")
    # the first row of file is skipped, because it is just labels and contains no data to be iterated through.
    next(fileIn)

    # this for loop iterates through the file and adds all of the vehicles with extreme mileages to a list.
    for line in fileIn:
        # the data is split with commas and stored within dList.
        dList = line.split(",")
        # the index 0 corresponds to the type of vehicle in the data.
        # all of the vans, trucks, and minivans are excluded from consideration.
        # this format is used to make reading the code easier.
        if dList[0] != 'VANS - CARGO TYPE' \
                and dList[0] != "SMALL PICKUP TRUCKS 2WD" \
                and dList[0] != "STANDARD PICKUP TRUCKS 2WD" \
                and dList[0] != "VANS - PASSENGER TYPE" \
                and dList[0] != "MINIVAN - 2WD" \
                and dList[0] != "MINIVAN - 4WD" \
                and dList[0] != "STANDARD PICKUP TRUCKS 4WD" \
                and dList[0] != "SMALL PICKUP TRUCKS 4WD":
            # the index 8 corresponds to the line with all the mileages listed.
            # if statement executes if the either maximum or minimum mileage is found.
            if val1 == int(dList[8]):
                # the vehicle label of the either minimum or maximum mileage are added to nList.
                # the indexes 1 and 2 represent the manufacturer and the car line to make up the whole label.
                nList.append(dList[1] + " " + dList[2])
    # the file is closed.
    fileIn.close()
    # the list with the vehicle labels of the maximum or minimum mileage is returned.
    return nList

# this function returns the maximum value of the list that contains the mileages of the cars.
# the parameter is the list that represents the data of the year chosen.
def maxVal(sList):
    return max(sList)

# this function returns the minimum value of the list that contains the mileages of the cars.
# the parameter is the list that represents the data of the year chosen.
def minVal(sList):
    return min(sList)

# this function takes the user's inputs and writes a new txt file with the max and min car mileages.
# the parameters are the name of the file, year chosen, list of max vehicles, list of min vehicles, max, and min.
# this function does not have a return.
def writeFile(fName, year, maxList, minList, maxNum, minNum):
    # the file is opened, and is set to the writing mode.
    fileIn = open(fName, "w")
    # the next two lines are printed at the beginning of the text file.
    fileIn.write("EPA City MPG Calculator " + year + "\n")
    fileIn.write("--------------------------------- \n")
    # the following for loop prints all of the mileages that are the maximum.
    fileIn.write("Maximum Mileage (city): " + str(maxNum) + "\n")
    for i in maxList:
        # the escape characters are used for easier readability.
        fileIn.write("\t" + i)
        fileIn.write("\n")
    # the following for loop prints all of the mileages that are the minimum.
    fileIn.write("Minimum Mileage (city): " + str(minNum) + "\n")
    for j in minList:
        # escape characters are used fro easier readability.
        fileIn.write("\t" + j)
        fileIn.write("\n")
    # this statement is printed to signify to the user that the text file was created with the chosen data.
    print("Operation Success! Mileage data has been saved to " + fName)

# the main function contains the questions that take the user's inputs and calls all the other functions.
def main():
    # the welcome statement is printed.
    print("Welcome to EPA Mileage Calculator")
    # the cont variable is set to the False Boolean in order to enter the while loop.
    cont = False
    # the following while loop executes to ask the user which year's data they would like to use.
    while not cont:
        # the user's choice is stored within this variable.
        year = input("What year would you like to view data for? (2008 or 2009): ")
        # the following if statement executes if the user enters a valid response.
        if year == "2008" or year == "2009":
            # cont is changed to True, so the while loop does not execute again.
            cont = True
            # based on the user's response the file is read and the mileages are stored in mList.
            # the readFile function is called, with the parameter of the file chosen by the user.
            if year == "2008":
                mList = readFile("epaVehicleData2008.csv")
            elif year == "2009":
                mList = readFile("epaVehicleData2009.csv")
        # if the user has an invalid response, then the else statement executes and the while loop runs again.
        else:
            print("*Invalid input, please try again!")

    # this variable store's the user's response of the name of the file that they want to store the results in.
    outFile = input("Enter the filename to save results to: ")
    # the maximum mileages are retrieved by calling the maxVal function with the mList parameter.
    maxNum = maxVal(mList)
    # the minimum mileages are retrieved by calling the minVal function with the mList parameter.
    minNum = minVal(mList)

    # the labels of the maximum/minimum mileages are stored in maxList and minList.
    # the readVal function is called, with the parameter of the file chosen, and the maximum/minimum mileages.
    if year == "2008":
        maxList = readVal("epaVehicleData2008.csv", maxNum)
        minList = readVal("epaVehicleData2008.csv", minNum)
    elif year == "2009":
        maxList = readVal("epaVehicleData2009.csv", maxNum)
        minList = readVal("epaVehicleData2009.csv", minNum)

    # writeFile function is called to write file with parameters of the file name, year, max/min vehicles and values.
    writeFile(outFile, year, maxList, minList, maxNum, minNum)
    # this statement is printed after the file is created and the program is over.
    print("Thanks, and have a great day!")

# the main function is called.
main()
