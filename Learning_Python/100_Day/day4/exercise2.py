# make program to select random name in list

names_string = "Gabriel, Annabel, Clarabel, Shalom, Syafa, Rayhan, Pabers, Farrel"

names = names_string.split(", ")
print("Daftar anggota undian pembayaran : ")
print(names)
print("Program sedang mengundi...")

import random

# get the total number of items in list
num_items = len(names)

# Generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items-1)

print("The person who has to pay all the bill is : ")
print(names[random_choice])
