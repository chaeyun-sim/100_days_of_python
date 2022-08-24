import os
import random
from art import logo

clear = lambda: os.system('clear')

my_cards = []
computer_cards = []
continue_game = True

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    pass
else:
    print("Goodbye!")
    quit()

clear()
print(logo)

def random_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    select = random.choice(cards)
    return select

for i in range(2):
    my_cards.append(random_cards())
computer_cards.append(random_cards())
if my_cards == 21:
    print('You win! Blackjack!')
    quit()

print(f"Your cards: [{my_cards[0]}, {my_cards[1]}]")
print(f"Computer's first card: {computer_cards}")


while continue_game == True:
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if get_another_card == 'y':
        my_cards.append(random_cards())
        computer_cards.append(random_cards())

        if sum(my_cards) >= 21:
            print("Your final hand : ", my_cards, "=", sum(my_cards))
            print("Computer's final hand: ", computer_cards, "=", sum(computer_cards))

            print("You lose!")
            quit()

        elif sum(computer_cards) >= 21:
            print("Your final hand : ", my_cards, "=", sum(my_cards))
            print("Computer's final hand: ", computer_cards, "=", sum(computer_cards))

            print("You win!")
            quit()

        else:
            print("Your cards: ", my_cards)
            print("Computer's cards: ", computer_cards)
            continue_game = True

    elif get_another_card == 'n':
        computer_cards.append(random_cards())
        continue_game = False
    else:
        print("\nError. You should type 'y' or 'n'.\n")
        quit()

print("Your final hand : ", my_cards, "=", sum(my_cards))
print("Computer's final hand: ", computer_cards ,"=", sum(computer_cards))

if 21 - sum(my_cards) < 21 - sum(computer_cards):
    print("You win!")
elif 21 - sum(my_cards) > 21 - sum(computer_cards):
    print("You lose!")
elif sum(my_cards) == sum(computer_cards):
    print("Draw")
