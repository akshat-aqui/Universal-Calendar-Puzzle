print("This program prints the day for a particular date")
import math
user_input = int()
def dooms_day(year):
    # dictionary to store days
    # value of anchor day can be known
    dict_day = {0: "Sunday",
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday"}

    # gregorian calendar repeats
    # every 400 years
    k = year % 400

    # decide the anchor day
    if (k >= 0 and k < 100):
        anchor = 2

    elif (k >= 100 and k < 200):
        anchor = 0

    elif (k >= 200 and k < 300):
        anchor = 5

    else:
        anchor = 3

    y = year % 100

    # dooms day formula by Conway
    doomsday = ((y // 12 + y % 12 + (y % 12) // 4) % 7 + anchor) % 7
    ######

    #storing the year in a list
    year = str(year)
    li = []
    for i in year:
        li.append(i)
    for y in range(2):
        li.pop(0)

    #function to change list to string
    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    s = li
    year_last_two = (listToString(s))
    year_last_two = int(year_last_two)

    divide = year_last_two / 12
    remainder = year_last_two % 12

    d = remainder / 4

    e = anchor + divide + remainder + d

    while e > 6:
        e = e - 7
    e = round(e)


    #doomsday(s)
    #These are the dates which have same days every year
    dday = 0
    if month == 1:
        year = int(year)
        if (year % 400 == 0) and (year % 100 == 0): #value changes for leap year
            dday = 4
        elif (year % 4 == 0) and (year % 100 != 0): #value changes for leap year
            dday = 4
        else:
            dday = 3

    if month == 2:
        year = int(year)
        if (year % 400 == 0) and (year % 100 == 0): #value changes for leap year
            dday = 29
        elif (year % 4 == 0) and (year % 100 != 0): #value changes for leap year
            dday = 29
        else:
            dday = 28
    if month == 3:
        dday = 14
    if month == 4:
        dday = 4
    if month == 5:
        dday = 9
    if month == 6:
        dday = 6
    if month == 7:
        dday = 11
    if month == 8:
        dday = 8
    if month == 9:
        dday = 5
    if month == 10:
        dday = 10
    if month == 11:
        dday = 7
    if month == 12:
        dday = 12

    a = (anchor)  # a
    b = (math.floor(divide))  # b
    c = (math.floor(remainder))  # c
    d = (int(d))  # d

    final_day = int(day)
    while final_day > 7:
        final_day -= dday
        final_day = abs(final_day)
    ans = a + b + c + d + final_day
    while ans >= 7:
        ans -= 7


    if ans == 0:
        dd = "Sunday"  # noneday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 1:
        dd = "Monday"  # oneday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 2:
        dd = "Tuesday"  # twosday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 3:
        dd = "Wednesday"  # threesday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 4:
        dd = "Thursday"  # foursday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 5:
        dd = "Friday"  # fivesday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))
    if ans == 6:
        dd = "Saturday"  # sixesday
        print("%s/%s/%s was a: %s " % (day, month, year, dd))

    return "End"

# Driver code
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(dooms_day(year))

#########################################################
