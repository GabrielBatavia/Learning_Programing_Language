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
    espresso = MENU["espresso"]
    espresso_cost = espresso["cost"]
    print(f"espresso : ${espresso_cost}")
    
    latte = MENU["latte"]
    latte_cost = latte["cost"]
    print(f"latte : ${latte_cost}")
    
    cappuccino = MENU["cappuccino"]
    cappuccino_cost = cappuccino["cost"]
    print(f"cappuccino : ${cappuccino_cost}")


# Main
print_menu()
user_order = input("What you want to order? espreso? latte? or cappuccino? : ")
