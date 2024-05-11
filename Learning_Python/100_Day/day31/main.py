# ---------------------------- RESOURCE ------------------------------- #

from tkinter import *
from tkinter import messagebox
import pandas as pd
import pyperclip
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./id_english_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# ---------------------------- ALL FUNCTION ------------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    english_word = current_card["inEnglish"]
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=english_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)
    

def flip_card():
    Indonesia_word = current_card["Indonesian"]
    canvas.itemconfig(card_title, text="Indonesia", fill="white")
    canvas.itemconfig(card_word, text=Indonesia_word, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
know_button = Button(image=check_image, command=is_known)
know_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()