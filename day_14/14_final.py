import random
import os
from game_data import data
from art import logo
from art import vs

clear = lambda: os.system('clear')

def to_list():
    A_data = random.choice(data)
    B_data = random.choice(data)

    if A_data == B_data:
            B_data = random.choice(data)

    A_info = []
    A_val = A_data.values()
    for item in A_val:
        A_info.append(item)

    B_info = []
    B_val = B_data.values()
    for item in B_val:
        B_info.append(item)
    return A_info, B_info


def check_answer(A_info, B_info, answer,score):
    score += 1
    if answer == 'A' and A_info[1] > B_info[1] or answer == 'B' and A_info[1] < B_info[1] :
        clear()
        print(logo)
        print(f"\nYou're right! Current score: {score}\n\n")

    elif answer == 'A' and A_info[1] < B_info[1] or answer == 'B' and A_info[1] > B_info[1] :
        clear()
        print(logo)
        print(f"\nSorry, that's wrong. Final score: {score}\n\n")
        quit()
            
    elif answer == 'A' and A_info[1] == B_info[1] or answer == 'B'and A_info[1] == B_info[1]:
        clear()
        print(logo)
        print("\nAmazing! The followers are both same!\n")

    else:
        print("\nYou typed the wrong answer. Restart the game.\n")
        quit()

    return score

score = 0
def the_game(score):
    print(logo)
    end_of_game = False
    while end_of_game == False:

        A_info = to_list()[0]
        B_info = to_list()[1]

        if A_info[0][0] == 'A' or A_info[0][0] == 'O' or A_info[0][0] == 'U' or A_info[0][0] == 'I' or A_info[0][0] == 'E':
            print(f"Compare A: {A_info[0]}, an {A_info[2]}, from {A_info[3]}")
        else:
            print(f"Compare A: {A_info[0]}, a {A_info[2]}, from {A_info[3]}")
        print(vs)
        print(f"Compare B: {B_info[0]}, a {B_info[2]}, from {B_info[3]}")

        answer = input("Who has more followers? Type 'A' or 'B' : ")

        clear()
        
        score = check_answer(A_info, B_info, answer, score)


the_game(score)