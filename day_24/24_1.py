# fname = open('./my_file.txt')
# fname.read()

import os
print(os.getcwd())

# file = open('day_24/my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# with open('day_24/my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# with open('day_24/data.txt', 'a') as file:
#     file.write("\n again New TEXT")

with open('./day_24/my_file.txt', 'a') as file:
    contents = file.read()
    print(contents)