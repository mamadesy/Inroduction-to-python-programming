import  os
os.system('cls')

def Swap(number_1, number_2):
    return number_2, number_1



a = 3
b = 4
print(a,b)
a,b = Swap(a,b)
print(a,b)