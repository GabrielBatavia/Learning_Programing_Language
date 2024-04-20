###### Scope ######

enemies = 1

def incrase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
incrase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

def drink_potion():
    potion_strengh = 2 # this call local variable
    print(potion_strengh)
    
drink_potion()
# print(potion_strengh) # We cant accses outside the function

# Global scope
player_health = 10 # this call global variable

def drink_potion2():
    potion_strengh = 2
    print(player_health)
    
drink_potion2()

