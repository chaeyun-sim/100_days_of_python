from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip

red = '#ff0000'

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white')


def password_generator():
    pw_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = []
    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)

    result = "".join(password_list)
    pw_input.insert(0, result)
    # pyperclip.copy()



def to_add():
    web = web_input.get()
    email = email_input.get()
    pw = pw_input.get()
    result = f"{web}  |  {email}  |  {pw}"
    print(result)

    if len(email) == 0 or len(web) == 0 or len(pw) == 0:
        warning = messagebox.showinfo(title='Error', message="Please make sure you have'nt left any of the fields empty.")
    else:
        check_info = messagebox.askokcancel(title=web, message=f'These are the detials entered: \n\nEmail: {email} \nPassword: {pw}\n\n Is it ok to save?')
        if check_info == True:
            with open(f"./day_29/data.txt", mode="a") as data_file:
                data_file.write(f"{result}\n")
                web_input.delete(0, END)
                email_input.delete(0, END)
                pw_input.delete(0, END)


# image canvas (tomato)
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
tomato_img = PhotoImage(file="./day_29/logo.png")
canvas.create_image(105, 100, image=tomato_img)
# canvas.pack()
canvas.grid(column=1, row=0)

web_text = Label(text="Website: ", bg='white')
web_text.grid(column=0, row=1)

email_text = Label(text="Email/Username: ", bg='white')
email_text.grid(column=0, row=2)

pw_text = Label(text="Password :", bg='white')
pw_text.grid(column=0, row=3)

web_input = Entry(width=35, highlightbackground='white')
web_input.insert(END, string="")
web_input.grid(column=1, row=1, columnspan = 2)

email_input = Entry(width=35, highlightbackground='white')
email_input.insert(END, string="")
email_input.grid(column=1, row=2, columnspan = 2)

pw_input = Entry(width=21, highlightbackground='white')
pw_input.insert(END, string="")
pw_input.grid(column=1, row=3)

generate_button = Button(width=10,text="Genearte Password", command=password_generator ,highlightbackground='white')
# generate_button.pack()
generate_button.grid(column=2, row=3)

add_button = Button(width=33,text="Add", command=to_add, highlightbackground='white')
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()