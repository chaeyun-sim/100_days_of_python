print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_direction = 0
second_direction = 0
last_direction = 0

print("You're at a crossroad, where do you want to go? Type 'left' or 'right'.")
if first_direction == 'left':
    print("'swim' or 'wait'?")
    if second_direction == 'wait':
        print("Which door? 'red', 'yellow', 'blue'")
        if last_direction == 'yellow':
            print("You Win!")
        elif last_direction == 'blue':
            print("Eaten by beasts. Game Over.")
        elif last_direction == 'red':
            print("Burned by fire. Game Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")



# 강의 코드

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
  choice2 = input('You\'ve came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
  if choice2 == "wait":
    choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
    if choice3 == "red":
      print("It's a rooom full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You entered a room of beasts. Game Over.")
    else:
      print("You choice a door that doesn't exist. Game Over.")
  else:
    print("You got attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over")