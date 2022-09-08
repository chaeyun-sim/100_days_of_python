from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(500, 500)

my_label = Label(text="This is old text")
my_label.config(text="This is new text")
my_label.pack()

# text
my_label["text"] = 'This is new text'
my_label.config(text="This is new text")

# if button is clicked
def action():
    print("Do something")

# button
button = Button(text="Click Me", command=action)
button.pack()

# textbox
input = Entry(width=30)
input.insert(END, string="Some text to begin with.") # click to edit
print(input.get())
input.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
# END - 언급하는 특정요소의 인덱스를 알아낼 수 있도록하는 것 (변경X)
print(text.get("1.0", END))
# 1.0 글자 0으로 시작하는 텍스트를 구하는 것
text.pack()

def spin_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spin_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
check = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
check.pack()

def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_1.pack()
radio_2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for i in fruits:
    listbox.insert(fruits.index(i), i)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()