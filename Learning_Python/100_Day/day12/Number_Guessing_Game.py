#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


# Resource and global variables
import random
from art import logo
numbers = list(range(1, 101))
choosen_numbers = 0
lives = 10
user_guess = 0
still_play = True


# All function here
def pick_numbers():
    return random.choice(numbers)

def check_the_guess():
    global still_play
    if user_guess > choosen_numbers:
        print("Your guess to High, Please try again")
    elif user_guess < choosen_numbers:
        print("Your guess to Low, Please try again")
    elif user_guess == choosen_numbers:
        print("Your guess Right! Congratulations you win the game")
        still_play = False

def play_game():
    global user_guess, lives, still_play
    
    if choosen_difficulty == "hard":
        lives = 5
    
    while still_play and lives > 0:
        print()
        print(f"You have {lives} lives to guess the number")
        user_guess = int(input("Take a guess : "))
        check_the_guess()
        lives -= 1 

# Main
print(logo)
print("Welcome to Number Guessing games!")
print("Im Thingking of number between 0 and 100")
choosen_numbers = pick_numbers()
print(f"The choosen numbers is {choosen_numbers}")

choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if choosen_difficulty == 'easy':
    play_game()
elif choosen_difficulty == 'hard':
    play_game()
else:
    print("Please enter a correct difficulty")
    exit()
