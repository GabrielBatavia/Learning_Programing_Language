# Resource
import random
lives = 6
from hangman_art import stages
from hangman_words import word_list 
from hangman_art import logo

print(logo)

# The program code
chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)

# Testing code
# print(f"Pssst, the solution is {chosen_word}")

# Create an empety list called display
display = []
for n in range(0, len(chosen_list)):
    print("_ ", end="", flush=True)
    display += "_"
    
print("")

end_of_game = False

while not end_of_game:
    print("")
    user_choose = input("Guess a letter : ")
    user_choose = user_choose.lower()
    
    # reveal the letter if its true
    for n in range(0, len(chosen_list)):
        letter = chosen_list[n]
        if user_choose == chosen_list[n]:
            display[n] = letter          
    
    if "_" not in display:
        end_of_game = True
        print("You WIN!!!")
    elif user_choose not in chosen_list:
        lives -= 1
        print(f"the letter {user_choose} not match")
        print("You loss one life!")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose...Game Over!")

    print(f"{' '.join(display)}")
    
    print(f"Your lives are {lives}")

print("")
print(display)

