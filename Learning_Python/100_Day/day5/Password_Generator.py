# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
easy_password = ""

# Easy level version
for n in range (0, nr_letters):
    random_letters = random.choice(letters)
    easy_password += random_letters
    
for n in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    easy_password += random_symbols

for n in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    easy_password += random_numbers


print(f"Your easy version password : {easy_password}")


# Hard level version

"""
all_nr = int(nr_letters) + int(nr_numbers) + int(nr_symbols) 
all_sources = [letters, symbols, numbers]

hard_password = ""

for n in range(0, all_nr):
    random_resource = random.choice(all_sources)
    random_password = random.choice(random_resource)
    
    hard_password += random_password
    
print(f"Your hard version password : {hard_password}")
"""

all_nr = int(nr_letters) + int(nr_numbers) + int(nr_symbols) 
hard_password = []
random_hard_password = ""

for n in range (0, nr_letters):
    random_letters = random.choice(letters)
    hard_password.append(random_letters)
    
for n in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    hard_password.append(random_symbols)

for n in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    hard_password.append(random_numbers)

for n in range(0, all_nr):
    random_password = random.choice(hard_password)
    random_hard_password += random_password

print(f"Your hard version password : {random_hard_password}")