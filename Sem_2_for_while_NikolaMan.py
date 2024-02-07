'''
Задача No9. Решение в группах
 По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
 (произведение всех чисел от 1 до N) 0! = 1 
 Решить задачу используя цикл while
 Input:       5
 Output:    120
'''
# n = int(input('Enter number: '))
# factorial = 1
# count = 1
#
# while count <= n:
#     factorial *= count
#     count += 1
#
# print(factorial)

# # второй способ:
# n = int(input('Enter number: '))
# factorial = 1

# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)

'''
Задача No11. Решение в группах
 Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
 то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
 Input:     5
 Output:  6

Ряд чисел Фибоначчи:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …
'''

# ## самостоятелбное решение
# A = int(input('Enter number A (more 0): '))

# fib_1 = 0
# fib_2 = 1
# fib_3 = fib_1 + fib_2
# count = 2

# while fib_3 < A:
#     fib_3 = fib_1 + fib_2
#     count += 1
#     temp = fib_2
#     fib_2 = fib_3
#     fib_1 = temp
    
# if fib_3 == A:
#     print(f'ф({count}) = {A}')
# else:      
#     print(f'{A} - не число из ряда Фибоначчи')


# # работа в группе
# A = int(input('Enter number A (more 0): '))

# fib_1 = 0
# fib_2 = 1
# fib_3 = fib_1 + fib_2
# count = 1

# while fib_1 < A:
#     fib_1 = fib_2
#     fib_2 = fib_3
#     fib_3 = fib_1 + fib_2
#     count += 1

# if fib_1 != A:
#     print(-1, f'{A} - не число из ряда Фибоначчи')
# else:
#     print(f'{count}-ое число из ряда Фибоначчи')


# ### оптимизация решения
# A = int(input('Enter number A (more 0): '))

# fib_1 = 0
# fib_2 = 1
# count = 2

# while fib_2 < A:
#     fib_1, fib_2 = fib_2, fib_1 + fib_2
#     count += 1

# if fib_2 != A:
#     print(-1, f'{A} - не число из ряда Фибоначчи')
# else:
#     print(f'{count}-ое число из ряда Фибоначчи')


# # решение Рустем Богданов
# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2

# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1
# print(i)


'''
Задача No13. Решение в группах
 Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
 за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, 
 занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась 
 самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура 
 ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе. 
 Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
 В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура 
 в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

 Input:    6 -> -20 30 -40 50 10 -10 
 Output: 2
'''

# from random import randint

# count = 0
# max_len = 0

# days = int(input('Enter number of days: '))
# for i in range(days): 
#     temp = randint(-50, 50)
#     print(temp, end=' ')
#     if temp > 0:
#         count += 1    
#         if count > max_len:
#             max_len = count
#     else:
#         count = 0
# print()
# print( 'day time: ', max_len)

# # 2-й вариант решения

# from random import randint

# count = 0
# max_len = 0

# days = int(input('Enter number of days: '))
# for i in range(days): 
#     temp = randint(-50, 50)
#     print(temp, end=' ')
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_len:
#             max_len = count
#         count = 0
# if count > max_len:
#     max_len = count
# print()
# print('day time: ', max_len)

# # Решение от Рустем Богданов
# n = int(input())
# k = 0
# max = 0

# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else:
#         if max < k:
#             max = k
#         k = 0

# print(max)


'''
15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза.
Все числа натуральные и не превышают 3000.
 Input:5 -> 5 1 6 5 9
 Output:1 9
'''

# from random import randint

# n = int(input('Enter number: '))

# min_n = 10
# max_n = 0

# min_n = float('inf')
# max_n = -float('inf')


# for _ in range(n):
#     weight = randint(1, 10)
#     print(weight, end=' ')
#     if weight > max_n:
#         max_n = weight
#     if weight < min_n:
#         min_n = weight
# print()
# print(min_n, max_n)


# # 2-й вариант решения

# from random import randint

# n = int(input('Enter number: '))

# weight = randint(1, 10)
# min_n = weight
# max_n = weight

# for _ in range(n - 1):
#     weight = randint(1, 10)
#     print(f'{weight}kg', end=' ')
#     if weight > max_n:
#         max_n = weight
#     if weight < min_n:
#         min_n = weight
# print()
# print(f'{min_n = } kg, {max_n = } kg')

# 3-й вариант решения

# from random import randint

# n = int(input('Enter number: '))

# weight = randint(1, 10)
# min_n = weight
# max_n = weight

# for _ in range(n):
#     weight = randint(1, 10)
#     print(f'{weight}kg', end=' ')
#     min_n = min(weight, min_n)
#     max_n = max(weight, max_n)
# print()
# print(f'{min_n = } kg, {max_n = } kg')

# ### Доп.занятие
# for num in range(50):
#     if num % 2 == 0:
#         continue
#     if num % 3 == 0:
#         print(num, end=' ')
#     if num == 33:
#         break
# else:
#     print('Я всё, закончил!')


# # решение Рустем Богданов
# n = int(input())
# max = -1
# min = 3001

# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x
#     if x < min:
#         min = x

# print(max, min)


'''
ДЗ
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.
Input: 5 -> 1 0 1 1 0 
Output: 2
'''

# from random import randint

# n = int(input('Enter odd number of coin: '))

# reshka = 0
# orel = 0

# for _ in range(n):
#     side = randint(0, 1)
#     print(side, end=' ')
#     if side == 0:
#         reshka += 1
#     else:        
#         orel += 1
# print()
# if reshka < orel:
#     print(f'reshka "0"=  {reshka}')
# else: print(f'orel "1"=  {orel}')

## Из теста
# coins = [1, 1, 1, 1, 0]

# reshka = 0
# orel = 0

# for i in range(len(coins)):
#     if coins[i] == 0:
#         reshka += 1
#         # print(coins[i])
#     else:
#         orel += 1

# if reshka < orel:
#     print(reshka)
# else:
#     print(orel)

# print(len(coins))

# # Решение из Теста

# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

'''
ДЗ
Задача 12:Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y ≤ 1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2 
5 6 -> 2 3
'''

# s = int(input('Enter sum of number: '))
# p = int(input('Enter producn of number: '))
# x = 0
# y = 0
# flag = True

# while flag:
#     for _ in range(s+1):
#         for _ in range(p+1):
#             # print('for', x, y)
#             if (x + y == s) and (x * y == p):            
                
#                 flag = False
#                 # print(x, y)
#                 # break            
#             y += 1
#         x += 1
#         y = 0
# print(x, y)
# # if (x + y != s) and (x * y != p):
# #     print(f'x {x}, y {y} - не подходят под наше условие')

# s = int(input('Enter sum of number: '))
# p = int(input('Enter producn of number: '))
# x = 0
# y = 0
# flag = True

# while flag:
#     if (x + y == s) and (x * y == p):          
                
#         flag = False
#         print(x, y)
#     for _ in range(s+1):
#         for _ in range(p+1):
#             # print('for', x, y)
            
#                 # print(x, y)
#                 # break            
#             y += 1
#         x += 1
#         y = 0
# print(x, y)
# # if (x + y != s) and (x * y != p):
# #     print(f'x {x}, y {y} - не подходят под наше условие')

### с помощником
# # Ввод суммы и произведения
# S = int(input("Введите сумму чисел S: "))
# P = int(input("Введите произведение чисел P: "))

# # Поиск подходящих значений для X и Y
# for x in range(1, 1001):
#     y = S - x
#     if x * y == P:
#         print(f"Задуманные числа: {x} и {y}")
#         break
# else:
#     print("Невозможно определить числа для заданных суммы и произведения.")

# из Теста:
# solution = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solution.append((min(i, j)), max(i, j))
# solution = list(set(solution))

# for solution in solution:
#     print(solution[0], solution[1])

        

'''
ДЗ
Задача 14:Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
Input: 10 -> 1 2 4 8
'''       
# n = int(input())
# x = 1

# while x <= n:
#     print(x)
#     x *= 2

# # из теста:
# i = 0
# while 2 ** i <= n:
#     print(2**i)
#     i += 1


    

    

            

