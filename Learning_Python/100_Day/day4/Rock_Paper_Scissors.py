# Rock Paper Scissors program
import random

print("Welcome to the Rock Paper Scissors Program")

user_guess = int(input("Please enter you guess: 1.Rock, 2.Paper, 3.Scissors: "))

program_aswer = random.randint(1, 3) 

if user_guess == program_aswer:
    print("You Win")
else :
    print("You losses")