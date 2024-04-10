# make program to check odd or even

number = int(input("Please enter your number : "))
age = int(input("Please enter your age : "))

if number % 2  == 0:
    print("This is an even number")
    
    if age >= 18:
        print("You have to pay 18$ for the ticket")
    else :
        print("Please pay 7$ for the ticket")
else :
    print("This is an odd number")