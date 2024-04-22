# Source
from game_data import data
import random
account = {}
compare_followers = 0

def get_compare():
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


# Main
account1 = get_compare()
account2 = get_compare()  
if account1 == account2:
    account2 = get_compare()


account_name_print(account1, account2)

