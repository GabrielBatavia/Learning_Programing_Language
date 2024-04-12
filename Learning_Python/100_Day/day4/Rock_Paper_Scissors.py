# Rock Paper Scissors program
import random

print("Welcome to the Rock Paper Scissors Program")

user_guess = int(input("Please enter you guess: 1.Rock, 2.Paper, 3.Scissors: "))

if user_guess == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif user_guess == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif user_guess == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
else :
    print("Please enter correct guess number")
    exit()

program_answer = random.randint(1, 3)

if program_answer == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif program_answer == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else :
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if user_guess == 1 and program_answer == 3:
    print("You Win")
elif user_guess == 1 and program_answer == 2:
    print("You lose")
elif user_guess == 1 and program_answer == 1:
    print("You tie")

if user_guess == 2 and program_answer == 1:
    print("You win")
elif user_guess == 2 and program_answer == 3:
    print("You lose")
elif user_guess == 2 and program_answer == 2:
    print("You tie")

if user_guess == 3 and program_answer == 2:
    print("You win")
elif user_guess == 3 and program_answer == 1:
    print("You lose")
elif user_guess == 3 and program_answer == 3:
    print("You tie")