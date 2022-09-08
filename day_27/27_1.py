from tkinter import *

window = Tk()

window.title("My first GUI program!")
window.minsize(500, 300)
window.config(padx=20, pady=20) # add padding

# if button is clicked
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

my_label = Label(text="I am a label", font=('Arial', 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

# text
my_label["text"] = 'New Text'
my_label.config(text="New Text")

# button
button1 = Button(text="Click", command=button_clicked)
# button.pack()
button1.grid(column=1, row=1)
button2 = Button(text="Me", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# textbox
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=3)


window.mainloop()