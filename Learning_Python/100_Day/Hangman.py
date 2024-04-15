# Step 4
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)

# Testing code
print(f"Pssst, the solution is {chosen_word}")

# Create an empety list called display
display = []
for n in range(0, len(chosen_list)):
    print("_ ", end="", flush=True)
    display += "_"
    
print("")

end_of_game = False

while not end_of_game:

    user_choose = input("Guess a letter : ")
    user_choose = user_choose.lower()

    # reveal the letter if its true

    for n in range(0, len(chosen_list)):
        letter = chosen_list[n]
        if user_choose == chosen_list[n]:
            print(f"{chosen_list[n]}", end="", flush=True)
            display[n] = letter
        else:
            print("_ ", end="", flush=True)
            
    print("")
    print(display)
    
    if "_" not in display:
        end_of_game = True

print("")
print(display)

