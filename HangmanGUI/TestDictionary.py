def main():
    novHolidays = ["Veteran's Day", "Thanksgiving"]
    decHolidays = ["Christmas", "New Year's Eve"]
    holidayList = [novHolidays, decHolidays]

    # 0 -> november, 1 -> december
    # print(holidayList[0]) # print november holidays
    # print(holidayList[1]) # print december holidays

    # create an empty dictionary
    # for the final project, mapping string -> list of MenuItem objects

    # mapping string -> list of strings
    holidays = {}
    holidays["November"] = ["Veteran's Day", "Thanksgiving"]
    holidays["December"] = ["Christmas", "New Year's Eve"]
    holidays["December"].append("Christmas Eve")

    holidays["December"] = ["Christmas Eve"]
    holidays["January"] = ["New Year's Day"]

    print(holidays["November"]) # print november holidays
    print(holidays["December"]) # print december holidays
    print(holidays["November"][0]) # print first holiday in november
    del holidays["December"] # remove the list associated with december

    holidays["November"].remove("Thanksgiving")




main()