# rock scissors paper!

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

my = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if my == 0:
  print(rock)
elif my == 1:
  print(paper)
elif my == 2:
  print(scissors)
else:
  print("Error. Wrong number.")


computer = random.randint(0,2)
print("Computer chose: ")

if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)


if computer == my:
  print("Same! Do it again.")
elif computer == 1 and my == 0 or computer == 2 and my == 1 or computer == 0 and my == 2:
  print("You lose")
else:
  print("You win!")



# ----------------------------- 강의 풀이
# 오류 체크까지 한 코드


import random

game_images = [rock, paper, scissors]

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed over 2. you lose!")
  quit()
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("You draw")