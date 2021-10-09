def neNol(numb):
    if numb > 0:
        return 1
    else:
        return 0
try:
    numb = int(input('Введите число: '))
    sist = int(input('Введите целевую систему счисления: '))
    while sist != 2 and sist != 8:
         print('Выберете либо 2-ичную систему счисления, либо 8-ичную: ')
         sist = int(input())
    if sist == 2:
        b = ''
        while neNol(numb) == 1:
            b = str(numb % 2) + b
            numb = numb // 2
        print(b)    
    if sist == 8:
        f = ''
        while neNol(numb) == 1:
            f = str(numb % 8) + f
            numb = numb // 8
        print(f)    
except ValueError: 
    print('Это не число. Введите число.') 

