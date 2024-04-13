# Make program that calculates sum of all the even numbers

target = int(input("Enter a number between 0 and 100 : "))
sum_target = 0
for n in range(0, target):
    
    if target > 0 :
        sum_target += target
        target -= 2
        #rint(target)

print(f"The sum of all the even numbers : {sum_target}")
    