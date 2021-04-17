import  random
import os
os.system('cls')


def Rand2D(a, b):
    n = random.randint(a+1, b+1)
    while n % 2 != 0:
        n = random.randint(a, b)
    return n



print(Rand2D(2, 6))

