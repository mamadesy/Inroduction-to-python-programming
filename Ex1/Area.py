import  math
import Swap
import  os
os.system('cls')


def Area(a, b, c, d):
    if d == 0:
        p = (a + b + c)/2
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

def AreaX(a, b, c, d):
    sides = [a, b, c, d]
    for i in range(len(sides)):
        if sides[i] == 0:
            sides.remove(sides[i])
            return Area(sides[0], sides[1], sides[2], 0)


print(Area(7, 6, 6, 0))
# print(AreaX(6, 6, 6, 0))
print(AreaX(6, 0, 4, 5))
