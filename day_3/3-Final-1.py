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

first_direction = input(
    "갈림길에 서있다. 어느 길로 가고 싶은가? '왼쪽' 또는 '오른쪽'을 입력하시오. ")
if first_direction == '왼쪽':
    print("너는 무사히 올바른 길로 갔다!")
    second_direction = input("강을 만났다. '수영' 또는 '기다린다'를 입력하시오. ")
    if second_direction == '기다린다':
        print("너는 무사히 강을 건넜다!.")
        last_direction = input("세 가지 문 중에 고르시오. '빨강', '노랑', '파랑' ")
        if last_direction == '노랑':
            print("너는 무사히 탈출했다")
            print("승리를 축하합니다!")
        elif last_direction == '파랑':
            print("너는 짐승들에게 물려 죽었다. 게임 오버. 다시 하세요.")
        elif last_direction == '노랑':
            print("너는 불 타 죽었다. 게임 오버. 다시 하세요.")
        else:
            print("게임 오버. 다시 하세요.")
    else:
        print("군사들에 의해 죽임을 당했다. 게임 오버. 다시 하세요.")
else:
    print("깊은 구덩이에 빠졌다. 게임 오버. 다시 하세요.")
