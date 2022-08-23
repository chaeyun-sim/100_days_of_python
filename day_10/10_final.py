from operator import not_
from art import logo
import os

clear = lambda: os.system('clear')

operations = ['+', '-', '*', '/']
end_of_calculation = False
go_to_first = True

while go_to_first == True:
    clear()
    print(logo)

    try:
        first_number = float(input("What's the first number?: "))
    except:
        print("\nValueError. You have you insert a float.\n")
        quit()
    go_to_first = False

    while go_to_first == False:
        
        operation = input("+\n-\n*\n/\nPick an operation: ")

        try:
            next_number = float(input("What's the ext number?: "))
        except:
            print("\nValueError. You have you insert a float.\n")
            quit()

        if operation == "+":
            result = first_number + next_number
        elif operation == "-":
            result = first_number - next_number
        elif operation == "*":
            result = first_number * next_number
        elif operation == "/":
            result = first_number / next_number
        else:
            print("Operation Error.")
            quit()

        print(f"\n{first_number} {operation} {next_number} = {result}\n")

        should_continue = input(f"Type 'y' to continue calculatison with {result}, or type 'n' to start a new calculation: ")

        if should_continue == 'y':
            first_number = result
            go_to_first = False
        elif should_continue == 'n':
            go_to_first = True
