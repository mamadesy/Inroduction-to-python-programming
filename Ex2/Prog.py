import  math
import os
os.system('cls')

def Mid_Even_Number1(a, b):
    result = []
    for i in range(a+1, b):
        if i%2==0:
            result.append(i)
    return result

def Mid_Even_Number2(a, b):
    result = []
    for i in range(min(a, b)+1, max(a, b)):
        if i%2==0:
            result.append(i)
    return result

def Is_Prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def Number_Divisor(n):
    result = []
    for i in range(1, n+1):
        if n%i==0:
            result.append(i)
    return result



print(Mid_Even_Number1(12,52))
print(Mid_Even_Number2(52,12))
print(Is_Prime(9))
print(Is_Prime(29))
print(Is_Prime(10026458))
print(Is_Prime(1002645895134691))
print(Number_Divisor(72))