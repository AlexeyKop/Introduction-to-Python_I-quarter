'''
# Задача No 17. Решение в группах.
#  Дан список чисел. Определите, сколько в нем встречается различных чисел.
#  Input: [1, 1, 2, 0, -1, 3, 4, 4]
#  Output: 6
'''
# import random 

# size = int(input('Enter size list:'))
# list_1 = []

# for _ in range(size):
#     num = random.randint(1, 10)
#     list_1.append(num)
# print(list_1)

# print()
# list_2 = []
# list_2 = [random.randint(1, 10) for _ in range(size)]
# print(list_2)

# # 1. Решение ч-з Множества
# print()
# set_1 = set (list_1)
# print(len(set_1))

# print()
# print(len(set(list_2)))
# print()

# 2.1 -е решение
# unique = []
# for num in list_1:
#     if num not in unique:
#         unique.append(num)
# print(len(unique))

# # 2.2 решение
# print()
# [unique.append(num) for num in list_1 if num not in unique]
# print('unique: ', unique)
# print(len(unique))

# 2.3 решение
# print()
# list_res = [list_2[i] for i in range (len(list_2)) if list_2[i] not in list_2[i + 1:]]
# print (len(list_res))

'''
# Задача No19. Решение в группах
#  Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
#  (сдвиг - циклический) на K элементов вправо,  K – положительное число.
#  Input:   [1, 2, 3, 4, 5] k = 3
#  Output:  [3, 4, 5, 1, 2]
'''

# 1-е решение
n = int(input('Enter amount number: '))
list_1 = [_ for _ in range(1, n + 1)]
print (list_1)
k = int(input('Enter number of shift (k): '))
print(list_1[-k:] + list_1[:-k])

# 2-е решение
for _ in range(k):
    # print(list_1.pop())
    last_num = list_1.pop()
    # print(list_1)
    list_1.insert(0, last_num)
print(list_1)

