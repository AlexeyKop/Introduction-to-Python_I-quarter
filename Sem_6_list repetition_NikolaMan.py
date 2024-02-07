'''
Задача No39. Решение в группах
Даны  два  массива  чисел.  Требуется  вывести  те  элементы первого  массива  
(в  том  порядке,  в  каком  они  идут  в  первом массиве), которых нет во втором массиве. 
Пользователь вводит число  N  -  количество  элементов  в  первом  массиве,  затем  N чисел  -  элементы  массива.  
Затем  число  M  -  количество элементов во втором массиве. Затем элементы второго массива
Ввод:               Вывод:
7                  3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
'''

# from random import randint

# n = int(input('введите длину 1-го массива: '))
# m = int(input('введите длину 2-го массива: '))

# # list_1 = []
# # list_2 = []

# # for _ in range(n):
# #     list_1.append(randint(1, 10))
# list_1 = [randint(1, 20) for _ in range(n)]
# print(list_1)

# set_2 = {randint(1, 20) for _ in range(m)}  # сгенерируем множ-во, чтоб не было повторяющ. элементов
# print(set_2)

# # res_list = []

# # for num in list_1:
# #     if num not in set_2:
# #         res_list.append(num)
# #         print(num, end=' ')

# res_list = [num for num in list_1 if num not in set_2]  # List Comprehension (Генератор списка)

# # res_list = [num if num not in set_2 else 0 for num in list_1]

# print()
# print(*res_list)

'''
Семинар 6. Повторение списков 
Задача No41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.
Ввод:           Ввод:
5               5 
1 2 3 4 5       1 5 1 5 1
Вывод:          Вывод:
0               2 
'''
# import random

# n = int(input('Enter number of list: '))
# list_1 = [random.randint(1, 5) for _ in range(n)]

# print(list_1)

# # count = 0
# # list_res = []
# # for i in range(1, len(list_1) - 1):
# #     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
# #         count += 1
# #         list_res.append(list_1[i])

# # print (count)
# # print(list_res)

# print([list_1[i] for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[i + 1]]) # List Comprehension (Генератор списка)

'''
Задача No43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:           Вывод:
1 2 3 2 3       2
'''

# from random import randint 

# n = int(input('Enter number of list: '))

# list_1 = [randint(1, 5) for _ in range(n)]
# print(list_1)

# count = 0
# # list_res = []
# # for i in range(len(list_1)):
# #     for j in range(i + 1, len(list_1)):
# #         if list_1[i] == list_1[j]:
# #             count += 1
# #             list_res.append(list_1[i])
# # 
# # print(count)
# # print(list_res)

### 2-й вариант ч-з ф-цию .count()

# for i in range(len(list_1)):
#     count += list_1[i + 1:].count(list_1[i])

# print(count)

# ### 3-й вариант (не учитывает повторные дубли)

# from random import randint

# n = int(input('Enter number of list: '))

# list_1 = sorted([randint(1, 5) for _ in range(n)])
# print(list_1)

# count = 0
# list_res = []
# el = list_1[0]
# for num in list_1[1:]:
#     if num == el:
#         count += 1
#         list_res.append(num)
#     else:
#         el = num

# print(count)
# print(list_res)

'''
Задача No45. Решение в группах
Два  различных  натуральных  числа n  и m  называются дружественными,  если  сумма  делителей  числа n 
(включая  1,  но  исключая  само n)  равна  числу m  и наоборот. 
Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
Программа получает  на  вход  одно  натуральное  число k,  не превосходящее  10**5.  
Программа  должна  вывести    все пары  дружественных  чисел,  каждое  из  которых  не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена  только  один  раз
(перестановка  чисел  новую пару не дает).
Ввод:       Вывод:
300         220  284
'''

# def sum_div(num):
#     summa = 1
#     for div in range(2, num // 2 + 1):
#         if num % div == 0:
#             summa += div
#     return summa

    # return sum(div for div in range(1, num) if num % div == 0)  # List Comprehension (Генератор списка)

# ## оптимизация def ч-з корень числа

# def sum_div(num):
#     summa = 1
#     sq_num = num ** 0.5
#     int_sq_num = int(sq_num)
#     if sq_num == int_sq_num:
#         summa += int_sq_num
#     for div in range(2, int_sq_num):
#         if num % div == 0:
#             summa += div + num // div
#     return summa

# k = int(input('Enter number: '))

# for num_1 in range(2, k):
#     num_2 = sum_div(num_1)
#     if num_1 < num_2 and num_1 == sum_div(num_2) and num_2 <= k:
#         print(num_1, num_2)

''' ДЗ
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность 
и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: a(n) = a(1) + (n-1) * d. 
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''
a1 = 7
n = 5
d = 2
# an = a1 + (n - 1) * d

# # if d > 0:
# #     for i in range(a1, an + 1, d):    
# #         print(i, end=' ')
# # else:
# #     for i in range(a1, an - 1, d):    
# #         print(i, end=' ')

print(*[_ for _ in range(a1, a1 + n * d, d)], sep='\n')

print(*range(a1, a1 + n * d, d))



# ### из ТЕСТА решение:
# for i in range(n):
#     print(a1 + i * d)




'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  6, 13
[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

# n = 6
# m = 13
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_index = []

# for i in range(len(list_1)):
#     if n <= list_1[i] <= m:
#         list_index.append(i)

# print(list_index)

# print(*[i for i in range(len(list_1)) if n <= list_1[i] <= m], sep='\n')   # List comprehensions



# ### из ТЕСТА решение:
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
