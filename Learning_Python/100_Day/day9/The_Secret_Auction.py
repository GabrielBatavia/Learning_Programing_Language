#from replit import clear
#HINT: You can call clear() to clear the output in the consol

input("Start the Program? yes or no : ")

# show the logo

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

for bid in auction_dict:
    max_bid = auction_dict[bid]
    
        
print(auction_dict)