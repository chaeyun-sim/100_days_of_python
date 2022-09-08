from tkinter import *

window = Tk()

window.title("My first GUI program!")
window.minsize(350, 100)
window.config(padx=20, pady=20) # add padding

text = Label(text="is equal to")
text.grid(column=0, row=1)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

def convert_miles_km():
    tmp = float(input.get())
    result = round(tmp * 1.609, 2)
    cal.config(text=f"{result}")

input = Entry(width=7)
input.grid(column=1, row=0)

cal = Label(text="0")
cal.grid(column=1, row=1)

# def button_clicked():
#     cal.config(text=calculated_number)

# cal.config(text=input.get())
# calculated_number = get_input * 1.609344

button1 = Button(width=7,text="Calculate", command=convert_miles_km)
button1.grid(column=1, row=2)

window.mainloop()