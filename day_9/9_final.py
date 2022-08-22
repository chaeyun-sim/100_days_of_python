# Secret auction excersice before answer\

from art import logo
import os

clear = lambda: os.system('clear')

clear()
print(logo)
print("Welcome to the secret auction program.")
print("Today's secret auction item is a necklace with 10 millennium star diamonds.")

names = []
bids = []
continue_auction = False

while continue_auction == False : 
    name = input("What is your name? ")
    names.append(name)
    bid = input("What is your bid? $")

    try:
        bid = int(bid)
    except ValueError:
        print("\nError! \nThe bid should be an integer number.\n")
        quit()

    bids.append(bid)
    other_people = input("Are there any other bidders? Type 'yes' or 'no'.\n")


    if other_people == 'no':
        continue_auction == True
        # print(names)
        # print(bids)
        
        di = dict(zip(names, bids))

        tmp = list()
        for k, v in di.items():
            the_tuple = (v, k)
            tmp.append(the_tuple)
        tmp = sorted(tmp, reverse=True)

        name_of_winner = tmp[0][1]
        bid_of_winner = tmp[0][0]


        clear()
        print(logo)

        print(f"\nThe winner is {name_of_winner} with a bid of ${bid_of_winner}.\n")

        quit()

    elif other_people == 'yes':
        clear()
        continue_auction == False