from xmlrpc.client import Boolean
from quiz import questions_data

correct_answer = []
quizs = []
done_quizes = []
input_is_wrong = True
cnt = 0
q_n = 1
is_going = True

def data():
    global questions_data
    for q in questions_data:
        quiz_quiz = q['question']
        quiz_answer = q['correct_answer']
        quizs.append(quiz_quiz)
        correct_answer.append(quiz_answer)


def check_answer(i, cnt, done_quizes, answer):
    if answer == correct_answer[i]:
        print("You got it right!")
        print(f"The correct answer was: {correct_answer[i]}")
        print(f"Your current score is: {cnt} / {len(done_quizes)}\n")
    elif answer != correct_answer[i]:
        print("That's wrong.")
        print(f"THe correct answer was: {correct_answer[i]}")
        print(f"Your current score is: {cnt - 1} / {len(done_quizes)}\n")
        cnt -= 1


def check_answer_right(answer):
    if answer.lower() not in ['true', 'false']:
        print("\nError! Wrong input!\n")
        quit()
    else:
        pass


data()


answer = input(f"Q.1: {quizs[0]}. (True/False): ")
check_answer_right(answer)


if is_going == True:
    for i in range(1, len(quizs) + 1):
        if i == (len(quizs)):
            print("\nAll done!")
            print(f"Your final result is : {cnt} / {len(done_quizes)}\n")
            is_going = False
            break

        q_n += 1
        cnt += 1
        done_quizes.append(quizs[i])

        check_answer(i, cnt, done_quizes, answer)

        new_answer = input(f"Q.{q_n}: {quizs[i]}. (True/False: ")
        check_answer_right(new_answer)
        answer = new_answer

        if i == (len(quizs) -1):
            check_answer()