#prompts
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter the day: "))

#check for leap year
def leapyear():
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return 1
    else:
        return 0

leapcheck = leapyear()

#months arrays
month31 = [1, 3, 5, 7, 8, 10, 12]
month31n = ["January", "March", "May", "July", "August", "October", "December"]

month30 = [4, 6, 9, 11]
month30n = ["April", "June", "September", "November"]

#check month length
def monthlength(m):
    if m in month31:
        return 31
    elif m in month30:
        return 30
    elif m == 2 and leapcheck == 1:
        return 29
    elif m == 2 and leapcheck == 0:
        return 28
    else:
        return 0

#initialize daycount
daycount = 0

#check and add month length up to the month prior to the one provided
for i in range(1,month):
    daycount += monthlength(i)

#add the day of the current month
daycount += day

#print result
print(daycount)