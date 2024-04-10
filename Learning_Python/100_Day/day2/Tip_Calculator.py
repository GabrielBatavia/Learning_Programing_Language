# Day 2 Project

print('Welcome to Tip calculator')
print("Please Input your bill :")
bill = input()

print('How much tip would you like to  give? 10, 12, or 15?')
tip = input()

cost_total = int(bill) * (int(tip) / 100 + 1)
print(f'You should pay {round(cost_total, 3)} including the tip')

print('')
print("Please input how many people will be pay")
num_people = input()

split_bill = cost_total / int(num_people)
split_bill = round(split_bill, 2)
print(f'Each person will pay {split_bill}')