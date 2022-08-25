import os
import random
import logo

clear = lambda: os.system('clear')
# lives = 0


def check_answer(guess, the_number, lives):
    """check if it's the right answer, or not."""
    if guess < the_number :
        print("Too low")
    elif guess > the_number :
        print("Too high")
    elif guess == the_number:
        print(f"\nYou got it! The answer was {the_number}\n")
        quit()


def check_difficulty(difficulty):
    """check the difficulty and when the game is hard, you have 10 lives, but if the game is easy, you have 5 lives."""
    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10
    else:
        print("\nError. You have to type 'easy' or 'hard'.\n")
        quit()
    return lives


def guess_the_number_game():
    """game part"""
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    the_number = random.randint(1, 101)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Type 'easy' or 'hard': ")
    lives = check_difficulty(difficulty)


    end_of_game = False
    while end_of_game == False:
        print(f"You have {lives} attempts remaining to guess the number.\n")
        lives -= 1

        try:
            guess = int(input("Make a guess: "))
        except:
            print("\nError! Guess a number.\n")
            quit()

        check_answer(guess, the_number, lives)
        print(f"Guess again.")

        if lives == 0:
            if guess == the_number:
                print(f"\nYou got it in the last turn! The answer was {the_number}\n")
            else:
                print(f"\nYou've run out of guesses, you lose.\nThe answer was {the_number}.\n")
            end_of_game = True


guess_the_number_game()