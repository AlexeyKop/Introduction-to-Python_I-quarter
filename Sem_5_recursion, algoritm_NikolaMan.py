'''
Числа Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,...
Задача No31. Решение в группах
Последовательностью   Фибоначчи   называется последовательность чисел a0, a1, ..., an, ..., 
где a0 = 0, a1 = 1, ak = a k-1 + a k-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# def fib(num):
#     if num == 1 or num == 2:
#         return 1        
#     return fib(num - 1) + fib(num - 2)

# n = int(input('Enter number: '))

# print(fib(n))

'''
Задача No33. Решение в группах
Хакер Василий получил доступ к классному журналу и хочет  заменить  все  свои  минимальные  оценки  на максимальные.   Напишите   программу,   которая заменяет   оценки   Василия,   но   наоборот:   все максимальные – на минимальные.
Input:5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
# import random

# def max2min(list_num):
#     max_num = max(list_num)
#     min_num = min(list_num)
#     while max_num in list_num:
#         i_max_num = list_num.index(max_num)
#         list_num[i_max_num] = min_num
#     # return list_num


# n = int(input('Enter the number of marks: '))
# marks = []

# # for _ in range(n):
# #     marks.append(random.randint(1, 5))

# marks = [random.randint(1, 5) for _ in range(n)]
# print(marks)

# max2min(marks)
# print(marks)

'''2-й вариант решения'''

# from random import randint
# import time

# n = int(input('Enter the number of marks: '))
# first_num = randint(1, 5)
# min_num = first_num
# max_num = first_num
# i_max_num = [0]

# start = time.time()
# marks = [first_num]

# for i in range(1, n):
#     num = randint(1, 5)
#     marks.append(num)
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
#         i_max_num = [i]
#     elif max_num == num:
#         i_max_num.append(i)

# print(marks)

# for i in i_max_num:
#     marks[i] = min_num

# end = time.time()
# dif = end - start

# print(marks)
# print(f'код работал {dif} секунд')

'''
Задача No35. Решение в группах
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n (само число)
Input: 5
Output: yes
'''
# def prime(n):
#     for div in range(2, n // 2 + 1):
#         if n % div == 0:
#             return False
#     return True

# num = int(input('Enter number: '))

# print(prime(num))

''' 2-е решение (оптимизация)'''

# def prime(n):
#     if n not in (2,3,5,7) and n % 2 == 0 and n % 3 == 0 and n % 5 == 0 and n % 7 == 0:   # проверяем число n на четность
#         return False
    
#     for div in range(11, int(n ** 0.5) + 1, 2): # извлекаем корень из числа n и в range увеличиваем шаг до 2
#         if n % div == 0:
#             return False
#     return True

# num = int(input('Enter number: '))

# print(prime(num))

'''
Задача No37. Решение в группах
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность 
в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input:    2 -> 3 4 5 6 
Output: 6 5 4 3 
'''

# def converse(num):
#     elem = int(input('Enter number: '))
#     if num == 1:
#         print(elem, end=' ')
#         return

#     converse(num - 1)
#     print(elem, end=' ')


# n = int(input('Enter the number of numbers in the sequence: '))

# converse(n)

# '''2-й вариант (оптимизированный)'''

# def revers_nums(num):
#     elem = input('Enter number: ')
#     if num == 1:
#         return elem + ' '        
#     return revers_nums(num - 1) + elem + ' '

# n = int(input('Enter the number of numbers in the sequence: '))

# print(revers_nums(n).strip())  # .strip() - убирает лишние пробелы


''' ДЗ
Задача 26:Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

# def degree (n, m):    
#     if m == 0:
#         return 1    
#     return n * degree(n, m - 1)

# # a = int(input('Enter number A: '))
# # b = int(input('Enter number B: '))

# # print(f'A ** B = {degree(a, b)}')

# # в автотесте такой вызов функции:
# print(degree(n = 2, m = 3))

''' ДЗ
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
2 2 => 4
'''
# def sum_num (n, m):
#     if m == 0:
#         return n       
#     return sum_num (n + 1, m - 1)


# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))

# print(f'a + b = {sum_num(a, b)}')

### Решение с теста:

# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)


### ===============================
# Помощник: 

# def sum_recursive(a, b):
#     if b == 0:
#         return a
#     elif b > 0:
#         return sum_recursive(a + 1, b - 1)
#     else:
#         return sum_recursive(a - 1, b + 1)

# # Пример использования
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# result = sum_recursive(num1, num2)
# print(f"Сумма чисел {num1} и {num2} равна {result}")

