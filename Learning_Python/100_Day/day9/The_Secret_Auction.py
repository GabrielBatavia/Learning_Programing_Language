#from replit import clear
#HINT: You can call clear() to clear the output in the consol

# Resource
from art import logo

start = input("Start the Program? yes or no : ")

if start == 'yes':
    
    # show the logo
    print(logo)
    
    # make the dictionary
    auction_dict = {}

    # make function to add to the dictionary
    def add_to_dict(name, bid_value):
        auction_dict[name] = bid_value 

    continue_program = True

    while not continue_program == False:
        
        # get username
        user_name = input("Enter your username : ")
        # get the bid
        user_bid = int(input("Enter your bid : $"))
        # Add to the dictionary
        add_to_dict(user_name, user_bid)

        user_choice = input("Are you want to continue the program? yes or no : ")
        if user_choice == "no":
            continue_program = False
        elif user_choice == "yes":
            continue_program = True
        else:
            print("Please enter the correct input, yes or no")
            continue_program = False

    highest_bid = 0
    for bidder in auction_dict:
        bid_amount = auction_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The higest bid is {highest_bid}, the winner is {winner}")
    

else:
    print("Good bye!")
    exit()