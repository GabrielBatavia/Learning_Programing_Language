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



# Python dosent have Block scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]  # we can create new variable inside if statment (python allow this)

print(new_enemy)

# but if

def create_enemy():
    if game_level < 5:
        new_enemy2 = enemies[0]

# print(new_enemy2)
# We got error in new_enemy2 cause its count as a local scope
