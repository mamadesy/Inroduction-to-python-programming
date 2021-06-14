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




# یک عدد اعشاری میگیرد و قسمت اعشاری آن را حذف میکند
def RemoveDecimal(decimalnumber):
    strnum = (str)(decimalnumber)
    result = 0
    powhelp = 1
    numlen = GetDecimalLen(PostiveNum(strnum))
    for i in strnum:
        if i.isdigit():
            result += (int)(i)*(10**(numlen-powhelp))
            powhelp += 1
        if i == '.':
            break
    if strnum[0] == '-':
        result *= -1
    return result



print(RemoveDecimal(195.5))
print(RemoveDecimal(-195.5))