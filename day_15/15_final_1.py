from main import MENU, resources

def select_coffee():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        ingredients = MENU[choice]['ingredients']
        print(f"water = {ingredients[0]}ml\nmilk = {ingredients[1]}ml\ncoffee = {ingredients[2]}g")

    while choice not in ("espresso", "latte", "cappuccino"):
        print("\nError! Invalid selection.\n")
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def resource_check(choice):
    contained = MENU[choice]['ingredients']
    return contained


def price_of_coffee(choice):
    if choice == 'espresso':
        coin = 1.50
    elif choice == 'latte':
        coin = 2.50
    elif choice == 'cappucchino':
        coin = 3.00
    return coin


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0,25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: "))  * 0.01
    total = float(quarters + dimes + nickels + pennies)
    return total


def money(price, payment):
    if price > payment:
        print("Sorry, that's not enough money. Money refunded!")
        return False
    elif price < payment:
        return True
    else:
        pass


def original_resources():
    global resources
    return list(resources.values())

def compare_resources(ordered):
    for item in ordered:
        if ordered[item] >= resources[item]:
            print("Sorry there is not enough {not_enough}.")
            return False
    return True


new_org = []
coffee_machine = True
while coffee_machine == True:

    your_coffee = select_coffee()
    
    ingredients = list(resource_check(your_coffee).values())
    og = original_resources()
    change = process_coins() - price_of_coffee(your_coffee)

    if new_org == []:
        print(f"Here is {change} in change.")
        print(f"Here is your {your_coffee} ☕ Enjoy!")

        if len(ingredients) != 3:
            for i in range(len(resource_check(your_coffee))):
                new_org.append(og[i] - ingredients[i])
        else:
            for i in range(len(resource_check(your_coffee))):
                new_org.append(og[i] - ingredients[i])
    elif compare_resources(new_org) == False:
        coffee_machine = False
    