import pandas



data = pandas.read_csv("./exercise3/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic_alphabet():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in alphabet please")
        generate_phonetic_alphabet()
    else:
        print(output_list)

# main
generate_phonetic_alphabet()