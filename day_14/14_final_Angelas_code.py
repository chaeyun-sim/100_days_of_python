from art import logo, vs
from game_data import data
import random
import os

clear = lambda: os.system('clear')


# Format the account data into printable format
"""takes the account data and return the printable format"""
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

## Use if statement to check if user iscorrect.
def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    elif a_followers < b_followers:
        return guess == "b"

# Display art
score = 0
print(logo)
game_should_continue = True
account_b = random.choice(data)


# make the game repeatable
while game_should_continue == True:
    # Generate a random account from the game data

    # Making the account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear the screen between rounds
    clear()

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's worng. Final score : {score}")