import time
from traceback import print_tb


def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        a = a // 2
        end = time.time()
        print(a, f"\nВремя затраченное на выполнение {end - start}")
    return wrapper


@deco
def SumNum(a, b, c, d):
    time.sleep(2)
    return a + b + c + d

SumNum(12, 25, 12, 1)