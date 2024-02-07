'''ФУНКЦИИ'''

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# sum_numbers(5)

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#     print('stop')

# # print(sum_numbers(5))

# a = sum_numbers(5, 'World') # Функция будет получать и обрабатывать те значения которые мы передаем
# print(a)

# # =====================================

# def sum_str(*args):  # * - если мы не знаем какое количество аргументов поступит
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('H', 'e', 'l', 'l','o'), sum_str('W', 'o', 'r', 'l', 'd'))
# print(sum_str('W', 'o', 'r', 'l', 'd'))

# # =======================================

'''МОДУЛЬНОСТЬ'''

# import Les_3_modul

# print(Les_3_modul.max_1(5, 9))


# from Les_3_modul import max_1

# print(max_1(15, 9))


# from Les_3_modul import * # * - вызывает все функции (чтоб не перечеслять все функции, которые мы хотим вызвать)

# print(max_1(15, 9))


# import Les_3_modul as m1 # через as можно переприсвоить имя модулю

# print(m1.max_1(5, 9))


'''РЕКУРСИЯ'''

# def fib(n):
#     if n in [1, 2]:     # ОБЯЗАТЕЛЬНО указываем БАЗИС (точка ОСТАНОВА), иначе происходит зацикливание и                        
#         return 1        # функция бесконечно вызывает сама себя
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))

# print(list_1)

''''АЛГОРИТМЫ'''
'''Быстрая сортировка'''

# def quick_sort(array):
#     if len(array) <= 1: # это БАЗИС нашей рекурсии - то место когда рекурсия будет завершать свою работу
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14, 58, 2, 10, 5, 8, 7]))

'''Сортировка слиянием'''
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2    # делим список до тех пор, пока не останется по 1 элементу
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0   # начинаем соединять все элементы воедино и упорядочивать
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1, 8, 4, 9, 7, 23, 2, 19]
merge_sort(list_1)
print(list_1)