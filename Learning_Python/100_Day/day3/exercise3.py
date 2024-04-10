#Build the program that check if its a leap year or normal year

year = int(input("Please enter a year : "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"so the year {year} is a leap year")
    elif year % 400 == 0:
        print(f"so the year {year} is a leap year")
    else :
        print(f"so the year {year} is not a leap year")
else :
    print(f"So the year {year} is not a leap year")