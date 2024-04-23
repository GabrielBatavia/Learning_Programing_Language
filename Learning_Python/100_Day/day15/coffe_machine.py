MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# All function

def print_menu():
    for drink, data in MENU.items():
        print(f"{drink} : ${data['cost']}")

def report_resources():
    for resource, amount in resources.items():
        print(f"{resource} : {amount}")
        
def check_resources(drink_ingredients):
    for item, amount_needed in drink_ingredients.items():
        if resources[item] < amount_needed:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def insert_money():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
    
def transaction(drink_name, drink_cost, payment):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
        

def make_coffee(drink_name, ingredients):
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")
        
# Main

while continue_program:
    
    get_resource()
    print_menu()
    user_order = input("What you want to order? espresso? latte? or cappuccino? : ")
    report_resources()
    insert_money()
    transaction()