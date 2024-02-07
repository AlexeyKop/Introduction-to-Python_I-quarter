'''
list_1 = []
list_2 = list()
list_3 = [1, 2, 3, 8]
# print(list_1)
# print(list_2)
print(list_3)
print(*list_3)

for i in list_3:
    print(i)

print(len(list_3))

print(list_3[-1])

list_3.append(12)
print(list_3)

print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

'''

# # 1.  Удаление последнего элемента списка.
# #  Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop() # - возвращает последний элемент
# print(a) # 0 
# print(list_1.pop())# 0 - удаляет последний элемент
# print(*list_1) # [12, 7, -1, 21]
# print(list_1.pop())# 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1)# [12, 7]

# # 2.  Удаление конкретного элемента из списка.
# #  Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(1))# 12 
# print(list_1) # [7, -1, 21, 0]

# # 3.  Добавление элемента на нужную позицию.
# #   Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]


# # Срез списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4,5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9,10]
# print(list_1[2:9]) # [3, 4,5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1,7]
# print(list_1[::6]) # [1, 7]


# ## КОРТЕЖ -  это неизменяемый список
# t = () # создание пустого кортежа
# print(type(t))  # class <'tuple'>
# t = (1,)        # в конце ставим запятую
# print(type(t))  # class <'tuple'>
# t = (1)
# print(type(t))  # <class 'int'>

# t = (28, 9, 1990)
# print(t)
# print(type(t))

# t = [28, 9, 1990]
# print(t)
# print(type(t))

# t = tuple(t)
# print(t)
# print(type(t))

# a, b, c = t # - распаковка кортежа
# print(a,b,c)

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# colors = ['red', 'green', 'blue'] # список
# print(colors)  # ['red', 'green', 'blue']

# t = tuple(colors) # преобразовали в кортеж
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])  # преобразовали в кортеж

# print(t[0]) # red
# print(t[2]) # blue

# for e in t:
#     print(e) # red green blue

# t[0] = 'black'# TypeError: 'tuple' object does notsupport (нельзя изменять кортеж)

# # Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))  #r:red g:green b:blue

# Словари
#  💡Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.

# dictionary = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d)
# print(d['q'])
# print(d['w'])

# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)   # {'up':'↑', 'left':'←', 'down':'↓','right':'→'}
# print(dictionary['left'])   # ←
# dictionary[895] = 98989
# print(dictionary)

# # типы ключей могут отличаться
# print(dictionary['up'])# ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])# ⇐
# print(dictionary['type'])# KeyError: 'type'
# del dictionary['left']   # удаление элемента
# for item in dictionary:
#     print(item)
#     print('{}: {}'.format(item, dictionary[item]))

# print(dictionary.items())   # выводит список, внутри которого кортежи, в кортеже: ключ, значение.
#                             # dict_items([('up', '↑'), ('left', '←'), ('down', '↓'), ('right', '→'), (895, 98989)])
# for (k,v) in dictionary.items():
#     print(k, v)
# # up: ↑
# # down: ↓
# # right: →

# # Множества
# #  💡Множества содержат в себе уникальные элементы,необязательно упорядоченные. 

# colors = {'red', 'green', 'blue'}
# print(colors)   # {'red', 'green', 'blue'}

# colors.add('red')
# print(colors)   # {'red', 'green', 'blue'}

# colors.add('gray')
# print(colors)   # {'red', 'green', 'blue','gray'}

# colors.remove('red')
# print(colors)   # {'green', 'blue','gray'}

# colors.remove('red')# KeyError: 'red' Выдает ошибку.
# colors.discard('red')   # ok. Проверяет, есть ли данное значение в нашем множестве. 
                        #Если оно есть, то удаляет, если нет, то не выдает ошибку.
# print(colors)   # {'green', 'blue','gray'}

# colors.clear()  # { } очищает все элементы из списка.
# print(colors)   # set()

# q = set()   # set() - создает множество
# print(q)


# # Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c = {1, 2, 3, 5, 8}
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)   # i = {8, 2, 5}  пересечение
# dl = a.difference(b)    # dl = {1, 3}
# dr = b.difference(a)    # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))  # {1, 21,3, 13}


# # Неизменяемое или замороженное множество(frozenset) — множество, с которым 
# # не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b)    # frozenset({1, 2, 3, 5, 8})


# List Comprehension (генератор списков)
# List comprehension — это упрощенный подход к созданию списка, который
#  задействует цикл for, а также инструкции if-else для определения того, что в итоге
#  окажется в финальном списке.

# 1.Простая ситуация — список:
# list_1 = [exp for item in iterable]

# 2.Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# # 1.Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)   # [1, 2, 3,..., 100]

# # # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,...,100]
# print(list_1)

# # 2.Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]   # [2, 4, 6,..., 100]
# print(list_1)

 
# # Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i*i ) for i in range(1,101) if i % 2 == 0]   #[(2,2),(4,4),..., (100, 100)]
# print(list_1)

# print()
# list_1 = [(i * 2, i / 2 ) for i in range(1,101) if i % 2 == 0]   # можно умножать, делить, прибавлять, вычитать.
# print(list_1)


 


 
