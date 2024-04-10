# Create a program using math and f string to calculate how many weeks we have left

print('How old are you now?')
age = input()

years = 90 - int(age)
week_left = years * 52

print(f"You have {week_left} weeks left in your life")
