# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Write your code below this line 
import math

def paint_calc(height, width, cover):
    number_cans = (height * width) / cover
    round_up_cans = math.ceil(number_cans)
    print(f"You'll need {round_up_cans} cans of point")
    
# Write your code above this line 
# Define a function called paint_calc() so the code below works.   

# Don't change the code below 
test_h = int(input("Input your height of wall : ")) # Height of wall (m)
test_w = int(input("Input your width of wall : ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

