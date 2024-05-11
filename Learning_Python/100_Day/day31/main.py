# ---------------------------- RESOURCE ------------------------------- #

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
know_button = Button(image=check_image)
know_button.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
know_button.grid(row=1, column=1)



window.mainloop()