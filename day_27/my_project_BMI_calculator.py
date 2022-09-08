from tkinter import *

window = Tk()

window.title("Calculate your BMI")
window.minsize(350, 150)
window.config(padx=30, pady=30) # add padding

height_text = Label(text="What is your height in m?")
height_text.grid(column=0, row=0)

weight_text = Label(text="What is your weight in kg?")
weight_text.grid(column=0, row=1)

m = Label(text="m")
m.grid(column=2, row=0)

kg = Label(text="kg")
kg.grid(column=2, row=1)

cal_text = Label(text="Your BMI is: ")
cal_text.grid(column=0, row=3)

result_text = Label(text="You are ")
result_text.grid(column=0, row=4)


def bmi_calculation():
    calculate_height = float(height.get())
    calculate_weight = float(weight.get())
    bmi_result = round(calculate_weight / (calculate_height**2), 1)

    if bmi_result <= 18.5:
        categories = "Underweight"
    elif bmi_result < 25:
        categories = "Normal weight"
    elif bmi_result < 30:
        categories = "Overweight"
    elif bmi_result >= 30:
        categories = "Obesity"

    cal.config(text=f"{bmi_result}")
    result.config(text=f"{categories}")


height = Entry(width=7)
height.grid(column=1, row=0)

weight = Entry(width=7)
weight.grid(column=1, row=1)

cal = Label(text="0")
cal.grid(column=1, row=3)

result = Label(text="None")
result.grid(column=1, row=4)

button1 = Button(width=7,text="Calculate", command=bmi_calculation)
button1.grid(column=1, row=2)


window.mainloop()


