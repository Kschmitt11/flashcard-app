from tkinter import *
import random

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

# Read CSV using pandas and convert to dictionary
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/spanish_to_english.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

curr_card = {}

# Functions
def next_card():
    canvas.itemconfig(card_id, image=flashcard_front)
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(title_id, text="Spanish", fill="black")
    canvas.itemconfig(word_id, text=curr_card["Spanish"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_id, image=flashcard_back)
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(word_id, text=curr_card["English"], fill="white")

def is_known():
    to_learn.remove(curr_card)
    content = pandas.DataFrame(to_learn)
    content.to_csv("data/words_to_learn.csv")
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)


# Flashcard Images
flashcard_front = PhotoImage(file="./images/card_front.png")
flashcard_back = PhotoImage(file="./images/card_back.png")

# Canvas settings
card_id = canvas.create_image(400,263, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_id = canvas.create_text(400, 150, text="Title", font=("Courier", 40, "italic"))
word_id = canvas.create_text(400, 263, text="Word", font=("Courier", 60, "bold"))

# Images
check_mark = PhotoImage(file="./images/right.png")
wrong_mark = PhotoImage(file="./images/wrong.png")



# Buttons
right_button = Button(image=check_mark, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_mark, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()



window.mainloop()

