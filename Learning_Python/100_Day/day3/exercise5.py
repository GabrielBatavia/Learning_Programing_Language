# build a program for love calculator

print("The Love calculator is calculating your score...")

name1 = input("Enter your name : ")
name2 = input("Enter their name : ")

combine_name = name1 + name2
lover_names = combine_name.lower()

t = lover_names.count("t")
r = lover_names.count("r")
u = lover_names.count("u")
e = lover_names.count("e")
first_digit = t + r + u + e

l = lover_names.count("l")
o = lover_names.count("o")
v = lover_names.count("v")
e = lover_names.count("e")
second_digit = l + o + v + e

total_love = int(str(first_digit) + str(second_digit))

if total_love < 10 and total_love > 90:
    print(f"Your score is {total_love}, you go together like coek and mentos")
elif total_love > 40 and total_love < 60:
    print(f"Your score is {total_love}, you are allright together")
else:
    print(f"Your score is {total_love}")

