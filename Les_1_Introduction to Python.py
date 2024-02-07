
# print(type(n))

# n = 'sk"\'dkfjs"fhs'
# print (n)
# print(type(n))

# n1 = "dfkas"
# print(n1)

# a = 5
# b = 1.89
# c = 'hello'
# print (a, '-', b, '-', c)
# print(f'{a} - {b} - {c}')
# print('{}-{}-{}'.format(a,b,c))

# print('Enter 1-st value ')
# a = input()
# print(type(a))
# b = input('Enter 2-nd value ')

# print(a, '+', b, '=', a + b)

# приведение типов данных
# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '159')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool (c)
# print(c)
# print(type(c))

# print('Enter 1-st value ')
# a = int(input())
# print(type(a))
# b = int(input('Enter 2-nd value '))

# print(a, '+', b, '=', a + b)

# a = 5.8954
# b = 6.4587
# print(round(a*b, 2))
# # round(1.56547, 2)

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter -4
# iter **= 5 # iter = iter ** 5


# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = "qwe"
# print (a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# username = input ('Enter name: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Hello Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Hi ', username)

i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('That\'s enough')
print(i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток от деления n на i = 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ''
# for i in range(5):
#     line = '=> '
#     for j in range(5):
#         line += '* '
#     print(line)

text = 'СъЕШь ещЁ этих МЯГКИХ французких БуЛоК'
# print(len(text))
# print('ещЁ' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещЁ', "ЕЩЩЩЁЁЁ"))

# print(text[len(text)-1])
# print(text[-1])
# print(text[:3])
# print(text[len(text)-10:])
# print(text[6:-5])
# print(text[0:len(text)-10:3])
# print(text[::3])
# print(text[2:9] + text[-5] + text[:6])
