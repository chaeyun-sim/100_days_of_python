from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)