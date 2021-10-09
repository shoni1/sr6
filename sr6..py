try:
    n = int(input('Введите кол-во элементов массива: ')) #Кол-во элементов массива
    a = [] #Создаем массив
    for i in range (n):
        a.append(int(input('Введите массив: '))) #Заполняем его
    delta = int(input('введите delta: ')) #Вводим дельту
    counter = 0 #Создаем счетчик отличающихся элементов
    for i in range (len(a)):
        if min(a) + delta == a[i]:
            counter += 1
    print(counter)
except ValueError: 
    print('Это не число. Введите число.')    
