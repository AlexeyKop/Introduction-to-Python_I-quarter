# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# # 1.
# res_list = list(filter(lambda x: x % 2 == 0, my_list))
# # print(*res_list)
# # print(list(res_list))
# print(res_list)

# # 2.
# res_list = []
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)

# # 3.
# f = lambda x: x % 2 == 0
# [el for el in my_list if f(el)] # List comprehension
# print(res_list)

# # функция map
# res_list = map(lambda x: x % 2 == 0, my_list)
# print(res_list)
# print(list(res_list))

'''
Задача No47. Решение в группах
У  вас  есть  код,  который  вы  не  можете  менять  (так  часто  бывает,  когда  код  в  глубине программы 
используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный  способ  вашего  взаимодействия  с  этим  кодом  -  посредством  задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите  такое  лямбда-выражение  transformation,  чтобы  transformed_values  получился копией values.

Ввод:
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

Вывод:
    ok
'''

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

'''
Задача No49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, 
орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники 
были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса 
орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
При решении задачи используйте списочные выражения. 
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''
# 1. (for in)
# def find_farthest_orbit(list_of_orbits):    
#     max_orbit = 0
#     for a, b in list_of_orbits:
#         if a != b:
#             if a * b > max_orbit:
#                 max_orbit = a * b
#                 a_b = a, b
#     return a_b, max_orbit

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# # 2-й вариант (List Compehension)

# def find_farthest_orbit(list_of_orbits):
#     list_of_ellips = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]
#     list_of_areas = [a * b for a, b in list_of_ellips]
#     max_s = max(list_of_areas)
#     i_max_s = list_of_areas.index(max_s)

#     return list_of_ellips[i_max_s], list_of_areas[i_max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# # 3-й вариант ч-з filter, map

# def find_farthest_orbit(list_of_orbits):
#     list_of_ellips = list(filter(lambda a_b: a_b[0] != a_b[1], list_of_orbits))
#     list_of_areas = list(map(lambda a_b: a_b[0] * a_b[1] ,list_of_ellips))
#     max_s = max(list_of_areas)
#     i_max_s = list_of_areas.index(max_s)

#     return list_of_ellips[i_max_s], list_of_areas[i_max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

'''
Задача No51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов 
отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:                                       Вывод:
values = [0, 2, 10, 6]                      same
if same_by(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')
'''
## 1-й вар
# def same_by(characteristic, objects):
#     print(set(map(characteristic, objects)))
#     return len(set(map(characteristic, objects))) < 2

# values = [0, 2, 10, 61]

# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

# ## 2-й вар (filter)
# def same_by(characteristic, objects):
#     new_list = list(filter(characteristic, objects))
#     print(f'{objects=}')
#     print(f'{new_list=}')
#     return objects == new_list or not new_list 
   
# values = [0, 23, 11, 61]

# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

# ## 3-й вар (map)
# def same_by(characteristic, objects):
#     new_list = list(map(characteristic, objects))
#     print(f'{objects=}')
#     print(f'{new_list=}')
#     return any(new_list) == all(new_list) or not new_list
    

# values = [0, 20, 10, 60]

# if same_by(lambda x: x % 2 == 0, values):
#     print('same')
# else:
#     print('different')

'''DZ
Задача 34:Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
Ввод:                                                 Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам                Парам пам-пам

'''

# def count_letters (word):
#     count = 0
#     vowels = 'а, у, о, ы, и, э, я, ю, ё, е'
#     for i in range(len(word)):
#         if word[i] in vowels:
#             count += 1
#     return count

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# flag = True

# # for i in range(len(stroka)):
# #     if ' ' not in stroka:
# #         print('Количество фраз должно быть больше одной!')
# #         break
# #     else:
# #         text_res = stroka.split()

# if ' ' in stroka:
#     text_res = stroka.split()
#     flag = True
#     for i in range(len(text_res) - 1):    
#         if count_letters(text_res[i]) != count_letters(text_res[i + 1]):
#             flag = False
    
#     if flag == False:
#         print('ритма нет')
#     else:        
#         print('ритм ЕСТЬ!')

# else:
#     print('Количество фраз должно быть больше одной!')    

# ### Решение из Теста
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()  # Метод .split () разделяет основную строку по разделителю и возвращает список строк.
# print('phrases=', phrases)
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []

# for i in phrases:
#     countVowels.append(len([x for x in i if x.lower() in vowels]))
#     # List comprehensions подсчитывает кол-во гласных в слове и создаёт из этого кол-ва список
# print('countVowels=', countVowels)  

# if countVowels.count(countVowels[0]) == len(countVowels): #.count() - используется для подсчета - сколько раз символ или подстрока встречаются в строке   
#     print('countVowels[0]=', countVowels[0])
#     print('len(countVowels)=', len(countVowels))
#     print('countVowels.count(countVowels[0])=',countVowels.count(countVowels[0]))
#     print('Есть ритм: Парам пам-пам')
# else:
#     print('нет ритма: Пам парам')

# ### 1-й вариант 

# def rifma(poem):
#     phrases_list = poem.lower().split()
#     sum_vowels = lambda phrase: sum(1 for symbol in phrase if symbol in 'аеёиоуыэюя')
#     tmp = sum_vowels(phrases_list[0])   # 4
#     if all([sum_vowels(phrase) == tmp for phrase in phrases_list[1:]]):
#         return 'Парам пам-пам'
#     return 'Пам парам'
    
# print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам'))

# ### 2-й вариант 

# def rifma(poem):
#     phrases_list = poem.lower().split()
#     sum_vowels = lambda phrase: len(list(filter(lambda symbol: symbol in 'аеёиоуыэюя', phrase)))
#     vowels_0 = sum_vowels(phrases_list[0])   # 4
#     if all(map(lambda phrase: sum_vowels(phrase) == vowels_0, phrases_list[1:])):
#         return 'Парам пам-пам'
#     return 'Пам парам'
    
# print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам'))

# ### 3-й вариант

# def cntVowLet(str):
#     cnt = 0
#     for let in str:
#         if let in vowLet:
#             cnt += 1
#     return cnt

# vowLet = "а, е, ё, и, о, у, ы, э, ю, я".split(",")

# inStr = input("Введите стихотворение Винни:")
# res = set(map(cntVowLet, inStr.split()))

# if len(res) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# ### 4-й вариант
    
# def sum_vowels(phrase):
#     vowLet = 'аеёиоуыэюя'
#     cnt = 0
#     for let in phrase:
#         if let in vowLet:
#             cnt += 1
#     return cnt

# def check_rifm(poem):
#     vowel_0 = sum_vowels(poem[0])
#     for phrase in poem[1:]:
#         if sum_vowels(phrase) != vowel_0:
#             return 'Пам парам'
#     return 'Парам пам-пам'

# check_rifm('пара-ра-рам рам-пам-папам па-ра-па-дам'.split())

# # text = input("Введите стихотворение Винни: ").split()
# # print(check_rifm(text))

'''
Задача 36:Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
у операции умножения.
Ввод:
print_operation_table(lambda x, y: x * y)

Вывод:
1         2         3         4           5         6
2         4         6         8           10       12
3         6         9         12          15       18
4         8         12        16          20       24
5        10         15        20          25       30
6        12         18        24          30       36
'''

# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return    
    
#     for row in range(1, num_rows + 1):
#         row_values = []       
#         for col in range(1, num_columns + 1):
#             element = operation(row, col)
#             row_values.append(element)  
#             # row_values.append(str(element))
#         # print(" ".join(row_values))
#         print(*row_values, sep=' ')
#         # print(row_values)

# # # Пример использования с операцией умножения
# # def multiplication_operation(row, col):
# #     return row * col

# # print_operation_table(multiplication_operation)
        
# print_operation_table(lambda x, y: x * y, 5, 5)