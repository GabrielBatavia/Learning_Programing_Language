# ---------------------------- RESOURCE ------------------------------- #

from tkinter import *
from tkinter import messagebox
import pandas as pd
import pyperclip
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./id_english_words.csv")
to_learn = data.to_dict(orient="records")


# ---------------------------- ALL FUNCTION ------------------------------- #

def next_card():
    current_card = random.choice(to_learn)
    english_word = current_card["inEnglish"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=english_word)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
know_button = Button(image=check_image)
know_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()