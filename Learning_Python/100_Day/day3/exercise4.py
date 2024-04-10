# buil automatic pizza order program

print("Thankyou for choosing Python Pizza delivery")
size = input("What suze pizza do you want? s, m, or l : ")

add_pepperoni = input("Do you want pepperoni? y or n : ")
extra_cheese = input("Do you want ectra cheese? y or n : ")

# make the bill
size_s = 15
size_m = 20
size_l = 25

cheese = 1


if size == "s":
    print(f"You order pizza size {size} and you bill get charge around {size_s}$")
    pepperroni = 0
    if add_pepperoni == "y":
        pepperroni = 2
        
    if extra_cheese == "y":
        total_bill = size_s + pepperroni + cheese
        print(f"You add additional pepperoni and cheese, your total bill is {total_bill}$")
    else :
        total_bill = size_s + pepperroni
        print(f"You add additional pepperoni, your total bill is {total_bill}$")

            
elif size == "m":
    print(f"You order pizza size {size} and you bill get charge around {size_m}$")
    pepperroni = 0

    if add_pepperoni == "y":
        pepperroni = 3
        
    if extra_cheese == "y":
        total_bill = size_m + pepperroni + cheese
        print(f"You add additional pepperoni and cheese, your total bill is {total_bill}$")
    else :
        total_bill = size_m + pepperroni
        print(f"You add additional pepperoni, your total bill is {total_bill}$")

else :
    print(f"You order pizza size {size} and you bill get charge around {size_l}$")
    pepperroni = 0

    if add_pepperoni == "y":
        pepperroni = 3
        
    if extra_cheese == "y":
        total_bill = size_l + pepperroni + cheese
        print(f"You add additional pepperoni and cheese, your total bill is {total_bill}$")
    else :
        total_bill = size_l + pepperroni
        print(f"You add additional pepperoni, your total bill is {total_bill}$")

