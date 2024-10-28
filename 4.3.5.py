#ask for month and year
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))


#check for leap year
def leapyear():
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return 1
    else:
        return 0

leapcheck = leapyear()


#store months in arrays
month31 = [1, 3, 5, 7, 8, 10, 12]
month31n = ["January", "March", "May", "July", "August", "October", "December"]

month30 = [4, 6, 9, 11]
month30n = ["April", "June", "September", "November"]


#check arrays/leapyear and tell amount of days
if month in month31:
    print(month31n[month31.index(month)] + " has 31 days")
elif month in month30:
    print(month30n[month30.index(month)] + " has 30 days")
elif month == 2 and leapcheck == 1:
    print(f"February has 29 days in {year}")
elif month == 2 and leapcheck == 0:
    print(f"February has 28 days in {year}")
else:
    print("None")