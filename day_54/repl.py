import time


def speed_calc_decorator(function):
    def func():
        current_time = time.time()
        func()
        times = time.time() - current_time
        print("{func.__name__} : ", times)

    return func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
