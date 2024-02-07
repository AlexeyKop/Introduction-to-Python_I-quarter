'''
# Задача No 17. Решение в группах.
#  Дан список чисел. Определите, сколько в нем встречается различных чисел.
#  Input: [1, 1, 2, 0, -1, 3, 4, 4]
#  Output: 6
'''

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(list_1)
# print(set(list_1))
# print(len(set(list_1)))

'''
# Задача No19. Решение в группах
#  Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
#  (сдвиг - циклический) на K элементов вправо,  K – положительное число.
#  Input:   [1, 2, 3, 4, 5] k = 3
#  Output:  [3, 4, 5, 1, 2]
'''

# list_1 = [1, 2, 3, 4, 5]
# k = int(input())
# k = k % len(list_1)

# list_res = []

# for i in range(k):
#     list_res.append(list_1[len(list_1) - k + i])
# print(list_res)

# for i in range(len(list_1) - k):
#     list_res.append(list_1[i])
# print(list_res)

'''
Задача No21. Решение в группах
 Напишите программу для печати всех уникальных значений в словаре. 
 Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
 {" V ":" S009 "}, {" VIII ":" S007 "}] 
 Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
#  {"V":" S009 "}, {"VIII":" S007 "}]

# set_1 = set()

# for i in list_1:
#     # print(i)
#     for j in i:
#         # print(j)
#         set_1.add(i[j])

# print(set_1)

'''
Задача No23. Решение в группах
 Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
 элементов массива, больших предыдущего (элемента с предыдущим номером) 
 Input: [0, -1, 5, 2, 3]
 Output: 2 (-1 < 5, 2 < 3)
'''

# list_1 = [0, -1, 5, 2, 3, 8, 12, 4]
# count = 0
# for i in range (len(list_1) - 1):       # for i in range (1, len(list_1)):
#     if list_1 [i + 1] > list_1 [i]:     # if list_1 [i] > list_1 [i-1]: 
#         count += 1
# print (count)

''' ДЗ
Задача 16:Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел A [i]. Последняя строка содержит число X.
'''

# # для решения Теста
# list_1 = [1, 2, 6, 3, 4, 5, 6]
# k = 6
# count = 0

# for i in range (len(list_1)):
#     if k == list_1[i]:
#         count += 1
# print(count)

# # др.вариант

# from random import randint

# n = int(input('Enter number of list: '))
# k = int(input('Enter number to search: '))
# count = 0

# list_1 = [randint(1, n) for i in range(n)]
# print(list_1)

# for i in range (len(list_1)):
#     if k == list_1[i]:
#         count += 1
# print(count)

# ## Тестовое решение
# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)



''' ДЗ
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел A [i]. Последняя строка содержит число X.
'''

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 6
# close_number = k
# min_dif = k

# for i in range(len(list_1)):
#     dif = abs(list_1[i] - k)
#     if dif < min_dif:
#         close_number = list_1[i]
#         min_dif = dif
# print(close_number)


# # Др.решение
# from random import randint

# n = int(input('Enter number of list: '))
# k = int(input('Enter number for find close number: '))
# min_dif = close_number = k

# list_1 = [randint(1, n) for i in range(n)]
# print(list_1)

# for i in range(len(list_1)):
#     dif = abs(list_1[i] - k)
#     if dif < min_dif:
#         close_number = list_1[i]
#         min_dif = dif
# print(close_number)

## Решение из ТЕСТА
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)



''' ДЗ
Задача 20:В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
 ●A, E, I, O, U, L, N, S, T, R – 1 очко; 
 ●D, G – 2 очка; 
 ●B, C, M, P – 3 очка; 
 ●F, H, V, W, Y – 4 очка; 
 ●K – 5 очков; 
 ●J, X – 8 очков; 
 ●Q, Z – 10 очков.

 А русские буквы оцениваются так:
 ●А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
 ●Д, К, Л, М, П, У – 2 очка; 
 ●Б, Г, Ё, Ь, Я – 3 очка; 
 ●Й, Ы – 4 очка; 
 ●Ж, З, Х, Ц, Ч – 5 очков; 
 ●Ш, Э, Ю – 8 очков; 
 ●Ф, Щ, Ъ – 10 очков.
 Напишите  программу,  которая  вычисляет  стоимость  введенного  пользователем  слова. 
 Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
 либо только русские буквы.
'''

## с Помощником

# def calculate_scrabble_score(word, language):
#     word = word.upper()  # Преобразуем все буквы в верхний регистр для унификации

#     scores = {
#         'ENGLISH': {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#                     'D': 2, 'G': 2,
#                     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#                     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#                     'K': 5,
#                     'J': 8, 'X': 8,
#                     'Q': 10, 'Z': 10},
#         'RUSSIAN': {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#                     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#                     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#                     'Й': 4, 'Ы': 4,
#                     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#                     'Ш': 8, 'Э': 8, 'Ю': 8,
#                     'Ф': 10, 'Щ': 10, 'Ъ': 10}
#     }

#     total_score = 0

#     for letter in word:
#         if letter in scores[language]:
#             total_score += scores[language][letter]
#         else:
#             print(f"Буква '{letter}' не поддерживается в выбранном языке.")

#     return total_score

# # Ввод слова и языка
# word = input("Введите слово: ")
# language = input("Введите язык (ENGLISH или RUSSIAN): ").upper()

# # Проверка введенного языка
# if language not in ('ENGLISH', 'RUSSIAN'):
#     print("Неверно указан язык. Поддерживаются только ENGLISH и RUSSIAN.")
# else:
#     score = calculate_scrabble_score(word, language)
#     print(f"Стоймость слова '{word}' в игре Скрабл: {score} очков.")


## Упрощенный вариант.
# scores = {
#      'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#                 'D': 2, 'G': 2,
#                 'B': 3, 'C': 3, 'M': 3, 'P': 3,
#                 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#                 'K': 5,
#                 'J': 8, 'X': 8,
#                 'Q': 10, 'Z': 10,
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#                 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#                 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#                 'Й': 4, 'Ы': 4,
#                 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#                 'Ш': 8, 'Э': 8, 'Ю': 8,
#                 'Ф': 10, 'Щ': 10, 'Ъ': 10
# }

# word = input("Введите слово: ").upper()

# total_score = 0

# for letter in word:
#     total_score += scores[letter]
# print(total_score)


# # Решение из теста
# k = 'ноутбук'

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)


