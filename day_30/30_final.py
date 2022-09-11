from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

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
    new_data = {
        web: {
            "email" : email,
            "password": pw,
        }
    }

    if len(email) == 0 or len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title='Error', message="Please make sure you haven't left any of the fields empty.")
    else:
        try:
            with open("./day_30/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./day_30/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # data = json.load(data_file)
            #Updating old data with new data
            data.update(new_data)

            with open("./day_30/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            email_input.delete(0, END)
            pw_input.delete(0, END)


def find_password():
    web = web_input.get()
    try:
        with open("./day_30/data.json", "r") as data_file:
            data = json.load(data_file)
            # print(data[web])
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found.")
    else:
        if web in data:
            matched_email = data[web]['email']
            matched_pw = data[web]['password']
            messagebox.showinfo(title=f'{web} information confirmed', message=f"Email: {matched_email}\nPassword: {matched_pw}")
        else:
            messagebox.showinfo(title='Error', message=f"No detailed information existed for {web}.")


# image canvas (tomato)
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
tomato_img = PhotoImage(file="./day_30/logo.png")
canvas.create_image(105, 100, image=tomato_img)
# canvas.pack()
canvas.grid(column=1, row=0)


# Labels
web_text = Label(text="Website: ", bg='white')
web_text.grid(column=0, row=1)

email_text = Label(text="Email/Username: ", bg='white')
email_text.grid(column=0, row=2)

pw_text = Label(text="Password :", bg='white')
pw_text.grid(column=0, row=3)


# Entries
web_input = Entry(width=21, highlightbackground='white')
web_input.insert(END, string="")
web_input.grid(column=1, row=1)

email_input = Entry(width=35, highlightbackground='white')
email_input.insert(END, string="")
email_input.grid(column=1, row=2, columnspan = 2)

pw_input = Entry(width=21, highlightbackground='white')
pw_input.insert(END, string="")
pw_input.grid(column=1, row=3)


# Buttons
search_button = Button(width=10, text="Search", highlightbackground= 'white', command=find_password)
search_button.grid(column=2, row=1)

generate_button = Button(width=10,text="Genearte Password", command=password_generator ,highlightbackground='white')
generate_button.grid(column=2, row=3)

add_button = Button(width=33,text="Add", command=to_add, highlightbackground='white')
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()