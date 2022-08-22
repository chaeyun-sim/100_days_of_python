for i in range(1, 101):
  if i % 3 == 0 and i % 15 != 0:
    print(i, "Fizz")
  elif i % 5 == 0 and i % 15 != 0:
    print(i, "Buzz")
  elif i % 15 == 0:
    print(i, "Fizzbuzz")
  else:
    print(i)


# 다른 버전
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("Fizzbuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)