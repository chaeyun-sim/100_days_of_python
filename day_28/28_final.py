from tkinter import *

pink = '#e2979c'
red = '#e7305b'
green = '#9bdeac'
yellow = '#f7f5dd'
font_name = 'Courier'
work_time = 25
short_break = 5
long_break = 20
reps = 0
timer = None


# UI setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=20, pady=20, bg=yellow)


# time reset
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_text.config(text="")
    reps = 0


# timer mechanism
def start_timer():
    global reps
    reps += 1
    
    work_sec = work_time * 60
    short_break_sec = short_break * 60
    long_break_sec = long_break * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=red)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=pink)
        mark = "✔" * int(reps / 2)
        # print(mark)
        check_text.config(text=mark)
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=green)
        

# countdown mechanism
def count_down(count):
    minutes = int(count / 60)
    # import math
    # math.floor(count/60)
    seconds = count % 60
    if seconds == 0 and minutes == 0:
        seconds = '00'
    elif 0 <= seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # mark = ""
        # work_sessions = int(reps/2)
        # for _ in range(work_sessions):
        #     mark += "✔"
        # check_text.config(text=mark)


# title label (Timer, Work, Break)
title_label = Label(text="Timer", font=(font_name, 50), bg=yellow, foreground=green)
title_label.grid(column=1, row=0)

# image canvas (tomato)
canvas = Canvas(width=250, height=224, bg=yellow, highlightthickness=0)
tomato_img = PhotoImage(file="./day_28/tomato.png")
canvas.create_image(123, 112, image=tomato_img)

# timer text (25:00, 5:00, 20:00)
timer_text = canvas.create_text(123, 130, fill='white', text="00:00", font=(font_name, 40, 'bold'))
canvas.grid(column=1, row=1)

# check if work time is over
check_text = Label(text="", font=(font_name, 35, 'bold'), bg=yellow, foreground=green)
check_text.grid(column=1, row=3)

# press Start to start the timer
start_button = Button(width=2,text="Start",highlightbackground=yellow, command=start_timer)
start_button.grid(column=0, row=2)

# press Reset to reset the timer
reset_button = Button(width=2,text="Reset", highlightbackground=yellow, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()