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

print(letter_index)