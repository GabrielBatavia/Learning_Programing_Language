# random module
import random

random_integer = random.randint(1, 10)
print(random_integer)

#import our module
import myModule
print(myModule.pi)

# random floating point numbers
random_float = random.random()
print(random_float)

random_float *= random_integer 
print(random_float)

# we can use it to our past project to get really easy way
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# List

states_of_america = ["Delaware", "Pennsylvania", "Raaahh"]

print(states_of_america[0])

# way to change contain list
states_of_america[1] = "Penn"

print(states_of_america)

# way to add something to the list
states_of_america.append("Angelaland")

print(states_of_america)

# extend the list
states_of_america.extend(["Angelaland", "Jackbauer"])
print(states_of_america)
