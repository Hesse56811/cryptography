import math
import sys
from one_way_alg import one_way_func
from Евклид import alg_evklid


a = int(input('Введите значение а = '))
b = int(input('Введите значение b = '))
p = int(input('Введите простое число р = '))

#Функция перевода числа из десятичной в двоичную

def int_to_bits(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b


#Функция проверки кривой на сингулярность

def singular_check(a, b):
    #уравнения для проверки на сигнулярность, для возведения в степень используем одностороннюю функцию
    y = (4 * one_way_func(a, 3, p) + 27 * one_way_func(b, 2, p)) % p
    if y == 0:
        print('Данная кривая сингулярна и не может быть рассмотрена')
        sys.exit()
    else:
        print('Данная кривая несингулярна')


# просим ввести порядок композиции
m = int(input('Введите порядок композиции, который необходимо найти, m = '))

# вводим начальную точку
x0 = int(input('Введите начальную координату х = '))
y0 = int(input('Введите начальную координату y = '))

# Находим точку, которая соответсвует нашей композиции

# функция нахождения двойной композиции
def double_point(x1, y1, a, p):
    k = ((3 * one_way_func(x1, 2, p) + a) * (alg_evklid(p, 2 * y1)[0] % p)) % p
    x3 = (k * k - 2 * x1) % p
    y3 = (k * (x1 - x3) - y1) % p
    return [x3, y3]


# функция нахождения суммы точек
def sum_point(x1, y1, x2, y2, p):
    k = ((y2 - y1) * (alg_evklid(p, x2 - x1)[0] % p)) % p
    x3 = (k * k - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return [x3, y3]

# преобразуем число композиции из десятичной в двоичную
bit_m = int_to_bits(m)


#print(bit_m)
#print(len(bit_m))


for i in range(len(bit_m), 0, -1):
    if i == len(bit_m):
        # Точка Q
        x = x0
        y = y0
    else:
        # строка 3 алгоритма из учебника: Q = [2]Q
        Q = double_point(x, y, a, p)
        x = Q[0]
        y = Q[1]
        # строка 4 алгоритма из учебника
        if bit_m[len(bit_m) - i] == '1':
            Q = sum_point(x0, y0, x, y, p)
            x = Q[0]
            y = Q[1]

# координаты итоговой точки
print(f'Получаем точку со следующими координатами x = {x}, y = {y}')

