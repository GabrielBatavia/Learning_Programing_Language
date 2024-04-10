print("Welcome to the rollercoaster!")
height = int(input('What is your height in cm? '))
age = int(input("Please enter your age : "))
ticket_bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    
    if age < 12:
        print("You have to pay 5$ for the ticket")
        ticket_bill = 5
    elif age <= 18:
        print("You have to pay 7$ for the ticket")
        ticket_bill = 7
    else :
        print("Please pay 12$ for the ticket")
        ticket_bill = 12
    
    print("Thankyou for buy the ticket, you want a photos and get extra 3$ charge?")
    photo = input("yes or no : ")

    total_bill = ticket_bill + 3

    if photo == "yes" :
        print("Thanks for the purchase")
        print(f"You total bill is {total_bill}$")
    else :
        print("Allright, please enjoy your rollercoaster")

else :
    print("You can't ride the rollercoaster, please grow taller")
    