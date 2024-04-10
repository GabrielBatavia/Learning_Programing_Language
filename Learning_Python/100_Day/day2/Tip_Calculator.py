# Day 2 Project

print('Welcome to Tip calculator')
bill = float(input("Please Input your bill $"))

tip = input("How much tip would you like to  give? 10, 12, or 15?")

cost_total = bill + (int(tip) / 100 * bill)
print(f'You should pay {round(cost_total, 2)} including the tip')

print("Please input how many people will be pay")
num_people = input()

split_bill = cost_total / int(num_people)
split_bill = round(split_bill, 2)
print(f'Each person will pay {split_bill}')