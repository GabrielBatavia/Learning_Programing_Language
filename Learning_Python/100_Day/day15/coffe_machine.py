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

# All function

def print_menu():
    global espresso_cost, cappuccino_cost, latte_cost
    
    espresso = MENU["espresso"]
    espresso_cost = espresso["cost"]
    print(f"espresso : ${espresso_cost}")
    
    latte = MENU["latte"]
    latte_cost = latte["cost"]
    print(f"latte : ${latte_cost}")
    
    cappuccino = MENU["cappuccino"]
    cappuccino_cost = cappuccino["cost"]
    print(f"cappuccino : ${cappuccino_cost}")

def report_resources():
    if user_order == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        
        print(f"water : {water}")
        print(f"milk : {milk}")
        print(f"coffee : {coffee}")

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
    global dolars
    
    if user_order == "espresso" and dolars > espresso_cost:
        print(f"Your total money : ${dolars}")
        print(f"espresso cost : ${espresso_cost}")
        
        dolars -= espresso_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
    
    elif user_order == "latte" and dolars > latte_cost:
        print(f"Your total money : ${dolars}")
        print(f"latte cost : ${latte_cost}")
        
        dolars -= latte_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
    
    
    elif user_order == "cappuccino" and dolars > cappuccino_cost:
        print(f"Your total money : ${dolars}")
        print(f"latte cost : ${cappuccino_cost}")
        
        dolars -= cappuccino_cost
        
        print(f"here is your changes : ${dolars}")
        print("Here you order")
    
    else:
        print(f"Your total money dosent enough")
        

def get_resource():
        espresso = MENU["espresso"]
        update_ingredients_esp = espresso["ingredients"]
         
        update_water_esp = update_ingredients_esp["water"]
        update_coffe_esp = update_ingredients_esp["coffe"]
        
        latte = MENU["latte"]
        update_ingredients_lat = latte["ingredients"]
        
        update_milk_lat = update_ingredients_lat["milk"]
        update_water_lat = update_ingredients_lat["water"]
        update_coffe_lat = update_ingredients_lat["coffe"]
        
        cappuccino = MENU["cappuccino"]
        update_ingredients_cap = cappuccino["ingredients"]
        
        update_milk_cap = update_ingredients_cap["milk"]
        update_water_cap = update_ingredients_cap["water"]
        update_coffe_cap = update_ingredients_cap["coffe"]


# Main
get_resource()
print_menu()
user_order = input("What you want to order? espresso? latte? or cappuccino? : ")
report_resources()
insert_money()
transaction()