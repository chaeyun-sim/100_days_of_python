# Who want's to pay the meal?


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

index = random.randint(1, len(names))

chosen = names[index]

print(f"{chosen} is going to buy the meal today!")

#----------------강의 풀이
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + "is going to buy the meal today.")