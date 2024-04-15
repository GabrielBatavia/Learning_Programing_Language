# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

# Todo-1 - Rnadomly choose a word from the word_list and assign it to a variab;e called chosen_word
chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)
print(chosen_word)
print(chosen_list)

# Todo-2 Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase
user_choose = input("Guess a letter : ")
user_choose = user_choose.lower()

# Todo-3 Check if the letter is the user guessed (guess) is one of the leters in the chosen_word
for n in range(0, len(chosen_list)):
    if user_choose == chosen_list[n]:
        print(chosen_list[n])
