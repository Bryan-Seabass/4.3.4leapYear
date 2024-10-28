year = int(input("Enter a year: "))

div4 = year % 4
div100 = year % 100
div400 = year % 400

if div4 == 0 and div100 != 0:
    print(f"{year} is a leap year")
elif div4 == 0 and div100 == 0 and div400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")