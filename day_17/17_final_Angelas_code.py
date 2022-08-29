from question_model import Question
from data import question_data
from quizes_brain import QuizBrain

# Question Attribute
# text, answer
# new_q = Question("2+3=5", "True")
# text = "2+3=5"
# answer = "True"

question_bank = []
for item in question_data:
    quiz_text = item["question"]
    quiz_answer = item["answer"]
    new_quiz = Question(quiz_text, quiz_answer)
    question_bank.append(new_quiz)

# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
