# Source
from game_data import data
import random
account = {}
compare_followers = 0

# All function

def get_compare():
    """This function will make random accounts for comparison

    Returns:
        _dict_: _the account of the famous person_
    """
    global account
    account = random.choice(data)
    return account

def account_name_print(first_account, second_account):
    account_name1 = first_account["name"]
    account_name2 = second_account["name"]
    account_desc1 = first_account["description"]
    account_desc2 = second_account["description"]
    
    print(f"The first account is {account_name1}, {account_desc1}")
    print(f"The first account is {account_name2}, {account_desc2}")
    
def compare_followers(compare, guess):
    accountcompare_followers = compare["follower_count"]
    accountguess_followers = guess["follower_count"]
    
    if accountcompare_followers > accountguess_followers:
        print("Your wrong")
    else:
        print("Your correct")


# Main
account1 = get_compare()
account2 = get_compare()  
if account1 == account2:
    account2 = get_compare()


account_name_print(account1, account2)

user_guess = input("Which one have more following accounts? 1 or 2? : ")

if user_guess == "1":
    user_account = account1
    compare_account = account2
else:
    compare_account = account1
    user_account = account2

compare_followers(compare_account, user_account)
