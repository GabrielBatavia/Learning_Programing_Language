# Make a function

def great(a, b):
    print("This your total amount")
    c = a + b 
    print(f"Your total amount is {c}")
    return c

great(10, 1000)
# print(c) #its dont work cause c is only in function

# function with input parameters
def greeting(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

names = input("Whats your name? : ")
greeting(names)

# function with more than one argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"I meet you at {location}")

loc = input("Please enter your location : ")
greet_with(names, loc)

# Keyword arguments
greet_with(name="Gabriel", location="Jakbar")