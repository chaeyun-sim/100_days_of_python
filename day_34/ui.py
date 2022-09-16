from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = Label(text=f"Score: 0", fg='white', bg=THEME_COLOR)
        self.scoreboard.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(150, 145, width=280, text="text", fill=THEME_COLOR, font=('Aria', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        false_img = PhotoImage(file="./100_days_of_python/day_34/images/false.png")
        true_img = PhotoImage(file="./100_days_of_python/day_34/images/true.png")

        self.if_right_button = Button(image=true_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.if_right)
        self.if_right_button.grid(column=0,row=2)
        
        self.if_wrong_button = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.if_wrong)
        self.if_wrong_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="🎉🎉 Congradulations! 🎉🎉\nYou've reached the end!")
            self.if_right_button.config(state='disable')
            self.if_wrong_button.config(state='disable')


    def if_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def if_wrong(self):
        if_answer_right = self.quiz.check_answer("False")
        self.give_feedback(if_answer_right)

    
    def give_feedback(self, right):
        if right == True:
            self.canvas.config(bg="green")
        elif right == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
