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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
choosen_numbers = 0
lives = 10
user_guess = 0
still_play = True


# All function here
def pick_numbers():
    return random.choice(numbers)

def check_the_guess():
    if user_guess > choosen_numbers:
        print("To High")
    elif user_guess < choosen_numbers:
        print("To Low")
    elif user_guess == choosen_numbers:
        print("You right")
    

def easy_games():
    global user_guess
    print(f"You have {lives} lives to guess the number")
    
    while still_play:
        for heart in range(1, lives):
            user_guess = int(input("Take a guess : "))
            print(check_the_guess())



# Main
print("Welcome to Number Guessing games!")
print("Im Thingking of number between 0 and 100")
choosen_numbers = pick_numbers()
print(f"The choosen numbers is {choosen_numbers}")

choosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if choosen_difficulty == 'easy':
    easy_games()
elif choosen_difficulty == 'hard':
    pass
else:
    print("Please enter a correct difficulty")
