print("Welcome to the rollercoaster!")
height = int(input('What is your height in cm? '))
age = int(input("Please enter your age : "))

if height >= 120:
    print("You can ride the rollercoaster")
    
    if age < 12:
        print("You have to pay 5$ for the ticket")
    elif age <= 18:
        print("You have to pay 7$ for the ticket")
    else :
        print("Please pay 12$ for the ticket")
else :
    print("You can't ride the rollercoaster, please grow taller")