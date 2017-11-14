import math


def primo(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if i < n and n % i == 0:
            return False
    return True


def primos(nn):
    k = 0
    num = 2
    while k < nn:
        if primo(num):
            print(num)
            k += 1
        num += 1


primos(10)