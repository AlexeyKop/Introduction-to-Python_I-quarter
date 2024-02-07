def tri(a, h):
    return 0.5 * a * h


def rect(a, b):
    return a * b


def circle(r):
    return 3.14 * r ** 2

# def main():
#     print('Начало модуля 1')
#     print('Начинаем считать площадь сложной фигуры')
#     area_1 = rect(20, 30) + tri(20, 15) - circle(5)
#     print(f'{area_1 = }')

#     print('Конец модуля 1')

# if __name__ == '__main__':  # проверяет, если модуль запускается из самого себя, то он попадает в этот if
#     main()

if __name__ == '__main__':  # 2-й вариант
    print('Начало модуля 1')
    print('Начинаем считать площадь сложной фигуры')
    area_1 = rect(20, 30) + tri(20, 15) - circle(5)
    print(f'{area_1 = }')

    print('Конец модуля 1')