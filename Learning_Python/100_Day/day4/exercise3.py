# Teasure map prorgram

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("Hidding you teasure: x marks the spot")
position = input("Where do you want to put the teasure? ")

# my code below
letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)

number_index = int(position[1]) - 1

map[number_index][letter_index] = "x"

print(f"{line1}\n{line2}\n{line3}")

