
def add(*arg):
    total = 0
    for n in arg:
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
# {'add': 3, 'multiply': 5}
# 25

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        # if non mathces, it returns None
        self.model = kw.get("model")

# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.make) # Nissan