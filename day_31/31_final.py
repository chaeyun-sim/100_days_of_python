from tkinter import *
from tkinter import messagebox
import pandas
import random


bg_color = '#b1ddc6'
current_word = {}
words_to_learn = {}


try:
    data = pandas.read_csv('./day_31/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("./day_31/french_words.csv")
    words_to_learn = original_data.to_dict(orient='records')
else:
    words_to_learn = data.to_dict(orient='records')


def next_word():
    global current_word
    global timer

    window.after_cancel(timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card)
    timer = window.after(3000, flip)


def next_word_known():
    words_to_learn.remove(current_word)
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("./day_31/words_to_learn.csv", index=False)

    if len(new_data) == 0:
        messagebox.showinfo(title='Congratulations!', message="Congratulations!\nThere is no words to learn!")
        quit()
    else:
        next_word()


def flip():
    canvas.itemconfig(title_text, text=f"English", fill='white')
    canvas.itemconfig(word_text, text=current_word["English"], fill='white')
    canvas.itemconfig(card_image, image=back_card)



# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=bg_color)
timer = window.after(3000, flip)


# card and button images
front_card = PhotoImage(file="./day_31/card_front.png")
back_card = PhotoImage(file="./day_31/card_back.png")
right_image = PhotoImage(file="./day_31/right.png")
wrong_image = PhotoImage(file="./day_31/wrong.png")


# upload image
canvas = Canvas(width=805, height=545, bg=bg_color, highlightthickness=0)
card_image = canvas.create_image(409, 268, image=front_card)


# text on image
title_text = canvas.create_text(400, 150, text="Title", font=('Aria', 40, 'italic'))

word_text = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


# buttons
right_button = Button(image=right_image, highlightbackground= bg_color, command=next_word_known)
right_button.grid(column=0,row=1)

wrong_button = Button(image=wrong_image, highlightbackground= bg_color, command=next_word)
wrong_button.grid(column=1,row=1)


next_word()

window.mainloop()
