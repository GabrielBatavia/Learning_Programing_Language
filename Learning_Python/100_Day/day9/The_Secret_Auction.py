#from replit import clear
#HINT: You can call clear() to clear the output in the consol

input("Start the Program? yes or no : ")

# show the logo

# make the dictionary
auction_dict = {}

# make function to add to the dictionary
def add_to_dict(name, bid_value):
    auction_dict[name] = bid_value 
    
# get username
user_name = input("Enter your username : ")
# get the bid
user_bid = int(input("Enter your bid : $"))

add_to_dict(user_name, user_bid)

print(auction_dict)