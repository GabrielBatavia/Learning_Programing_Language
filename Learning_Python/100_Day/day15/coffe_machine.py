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

dolars = 0
espresso_cost = 0
latte_cost = 0
cappuccino_cost = 0
status_order = False
continue_program = True

update_water_esp = 0
update_coffee_esp = 0

update_milk_lat = 0
update_water_lat = 0
update_coffee_lat = 0

update_milk_cap = 0
update_water_cap = 0
update_coffee_cap = 0


# All function

def print_menu():
    for drink, data in MENU.items():
        print(f"{drink} : ${data['cost']}")

def report_resources():
    for resource, amount in resources.items():
        print(f"{resource} : {amount}")

def insert_money():
    global dolars
    
    print("Please insert coins")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    penny = int(input("How many penny? : "))
    
    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.10
    nickels_amount = nickels * 0.05
    penny_amount = penny * 0.01
    dolars = quarters_amount + dimes_amount + nickels_amount + penny_amount
    print(f"Your total money : ${dolars}")
    
def transaction():
    global dolars, status_order, continue_program
    
    if user_order == "espresso" and dolars > espresso_cost:
        print(f"Your total money : ${dolars}")
        print(f"espresso cost : ${espresso_cost}")
        
        dolars -= espresso_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
        status_order = True
    
    elif user_order == "latte" and dolars > latte_cost:
        print(f"Your total money : ${dolars}")
        print(f"latte cost : ${latte_cost}")
        
        dolars -= latte_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
        status_order = True
    
    
    elif user_order == "cappuccino" and dolars > cappuccino_cost:
        print(f"Your total money : ${dolars}")
        print(f"latte cost : ${cappuccino_cost}")
        
        dolars -= cappuccino_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
        status_order = True
    
    else:
        print(f"Your total money dosent enough")
        continue_program = False
        

def get_resource():
    global update_water_esp, update_coffee_esp
    global update_milk_lat, update_water_lat, update_coffee_lat
    global update_milk_cap, update_water_cap, update_coffee_cap
    
    espresso = MENU["espresso"]
    update_ingredients_esp = espresso["ingredients"]
         
    update_water_esp = update_ingredients_esp["water"]
    update_coffee_esp = update_ingredients_esp["coffee"]
        
    latte = MENU["latte"]
    update_ingredients_lat = latte["ingredients"]
        
    update_milk_lat = update_ingredients_lat["milk"]
    update_water_lat = update_ingredients_lat["water"]
    update_coffee_lat = update_ingredients_lat["coffee"]
        
    cappuccino = MENU["cappuccino"]
    update_ingredients_cap = cappuccino["ingredients"]
        
    update_milk_cap = update_ingredients_cap["milk"]
    update_water_cap = update_ingredients_cap["water"]
    update_coffee_cap = update_ingredients_cap["coffee"]
        

def update_resource():
    global resources, status_order
    
    if user_order == "espresso" and status_order == True:
        resources["water"] = resources["water"] - update_water_esp
        resources["coffee"] = resources["coffee"] - update_coffee_esp
        
        print(resources["water"])
        print(resources["coffee"])
        
    elif user_order == "latte" and status_order == True:
        resources["milk"] = resources["milk"] - update_water_lat
        resources["water"] = resources["water"] - update_milk_lat
        resources["coffee"] = resources["coffee"] - update_coffee_lat

        print(resources["milk"])
        print(resources["water"])
        print(resources["coffee"])

    elif user_order == "cappuccino" and status_order == True:
        resources["milk"] = resources["milk"] - update_milk_cap
        resources["water"] = resources["water"] - update_water_cap
        resources["coffee"] = resources["coffee"] - update_coffee_cap
        
        print(resources["milk"])
        print(resources["water"])
        print(resources["coffee"])

# Main

while continue_program:
    
    get_resource()
    print_menu()
    user_order = input("What you want to order? espresso? latte? or cappuccino? : ")
    report_resources()
    insert_money()
    transaction()