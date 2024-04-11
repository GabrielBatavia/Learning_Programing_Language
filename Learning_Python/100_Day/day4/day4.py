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