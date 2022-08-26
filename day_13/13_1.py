# Problem 1
# Problem : the range i produces from 1 to 19
# Solution : the range should be range(1, 21)

def my_function():
#   for i in range(1, 20):
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()


# Problem 2
# Problem : the randint produces from 1 to 5, but the first index in the list is [0]
# 1 Solution : change the randint range to (0, 5)
# 2 Solution : insert 'dice_num -= 1' after randint. Then the result will be 0~5

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# Problem 3
# Problem : if you type '1994' as an answer of year, either if statement or elif statement doesn't contain 1994.
# Solution : make the if statement contain 1994

year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")


# Problem 4
# Problem : age is string, so it can't calculate with integer
# Solution : make the input(string) as a integer

# age = input("How old are you?")
age = int(input("How old are you? "))
if age > 18:
	print(f"You can drive at age {age}.")


# Problem 5
# Problem : == is a boolean operator. it produces True and False, so total_words can't be printed.
# Solution : change == to =

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Problem 6
# Problem : as the append function is out of for loop, it append nothing. Also if the blank_list is in the function, it doesnt' work.
# Solution : the b_list has to append the items in a_list, so it have to do an indentation. And also the blank list of b_list should be out of the function.

b_list = []
def mutate(a_list):
# b_list = []
  for item in a_list:
    new_item = item * 2
# b_list.append(new_item)
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])


# Fizzbuzz Error
# The Fizzbuzz has to Fizz when divided in 3 and Buzz when divided in 5, Fizzbuzz when divided in 15.
# Problem : the code prints Fizzbuzz when the number divides by 3 or 5.
# Solution : change or to and, so that the number can be divided by 3 and 5 (15).  And also 3 ifs should change to if - elif.

for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
    if number 5 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # if number % 3 == 0:
    elif number % 3 == 0:
        print("Fizz")
    # if number % 5 == 0:
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])