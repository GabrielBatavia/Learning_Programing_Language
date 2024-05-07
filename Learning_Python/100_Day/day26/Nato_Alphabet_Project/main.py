import pandas as pd

data = pd.read_csv('./Nato_Alphabet_Project/nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Input your word : ").upper()

user_alphabet = [data_dict[letter] for letter in user_word]

print(user_alphabet)