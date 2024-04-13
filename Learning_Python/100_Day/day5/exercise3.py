# Make program that calculates sum of all the even numbers

target = int(input("Enter a number between 0 and 100 : "))
sum_target = 0
for n in range(2, target + 1, 2):
        sum_target += n
        #target -= 2
        #print(target)

print(f"The sum of all the even numbers : {sum_target}")
    