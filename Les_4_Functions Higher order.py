'''lambda - функции'''
# def f(x):
#     return x * x

# a = f # а - переменная, которая хранит в себе ссылку на функцию  
# print(a(5))
# print(f(5))

# def calk_1(a, b):
#     return a + b

# calk_1 = lambda a,b: a + b  # можно сократить предыдущую функцию def calk_1(a, b) 

# def calk_2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 10)
# math(calk_2, 5, 10)

'''
1.В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар(число; квадрат числа).
Пример:1 2 3 5 8 15 23 38
Получить:[(2,4), (8,64), (38,1444)]
'''

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2)) # передаем в виде кортежа 

# print(res)        

# ## тоже самое, через lambda фнкцию

# def select(f, col): # возвращает список, к каждому элементу которого применили ф-цию f
#     return [f(x) for x in col]

# def where(f, col):  # возвращает только те значения, которые прошли проверку условия f(x) 
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)

# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

'''Функция map'''
# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

'''
Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
'''
### функция строка.split() - создает список из значений строки

# data = '15 156 96 3 5 74 6 45'
# print(data)

# # data = data.split() # выводит список строк
# # print(data)

# data = list(map(int, data.split())) # к каждому объекту применяем ф-цию int
# print(data)

### ==========================
# предыдущ задачу можно решить с помощью map:

# # def select(f, col): # возвращает список, к каждому элементу которого применили ф-цию f
# #     return [f(x) for x in col]

# def where(f, col):  # возвращает только те значения, которые прошли проверку условия f(x) 
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)  # заменяет ф-цию select
# print(res)

# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = list(map(lambda x: (x, x ** 2), res))   # заменяет ф-цию select
# print(res)

'''Функция filter'''
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# def where(f, col):  # возвращает только те значения, которые прошли проверку условия f(x) 
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# # print(res)

# res = filter(lambda x: x % 2 == 0, res) # заменяет ф-цию where 
# # print(res)

# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''Функция zip'''
# users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
# ids = [4, 5, 9, 14, 7] 
# data = list(zip(users, ids)) 
# print(data)

# # Функцияzip()пробегает по минимальному входящему набору:

# users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
# ids = [4, 5, 9, 14, 7] 
# salary = [111, 222, 333] 
# data = list(zip(users, ids, salary)) 
# print(data)

'''Функция enumerate'''

# Функцияe numerate() позволяет пронумеровать набор данных.

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

'''ФАЙЛЫ'''

# # 1.Режим a

# colors = ['red', '888978', 'blue']
# data = open('file.txt', 'a')    # здесь указываем режим,в котором будем работать
# data.writelines(colors)         # разделителей не будет
# data.close()    # используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.

# # Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# print(56)

# # 2.Режим r Чтение данных из файла:

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# # 3.Режим w

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()