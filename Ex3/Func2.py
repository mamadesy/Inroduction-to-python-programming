import os
os.system('cls')


#طول یک عدد اعشاری را برمیگداند
def GetDecimalLen(deciamlnum):
    numlen = 0
    for i in range(len(deciamlnum)):
        if deciamlnum[i]=='.' :
            break
        numlen += 1
    return numlen





# یک رشته حرفی که شامل یک عدد میباشد به عنوان ورودی میگیرد و مقدار مثبت آن عدد را برمیکرداند
def PostiveNum(strnumber):
    if strnumber.startswith('-'):
        return (str)(strnumber).removeprefix('-')
    return strnumber


#یک رشته حرفی شامل یک عدد اعشاری را میگیرد و آن را به یک عدد تبدیل میکند
def ConvertStrToDouble(strnumber):
    result = 0
    powhelp = 1
    numlen = GetDecimalLen(PostiveNum(strnumber))
    for i in strnumber:
        if i.isdigit():
            result += (int)(i)*(10**(numlen-powhelp))
            powhelp += 1
    if strnumber[0] == '-':
        result *= -1
    return result


print(ConvertStrToDouble('192.34'))
print(ConvertStrToDouble('-192.34'))
print(ConvertStrToDouble('-16.6587'))
print(ConvertStrToDouble('192'))
print(ConvertStrToDouble('-192'))