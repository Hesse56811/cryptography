from math import sqrt
from itertools import islice
from one_way_alg import one_way_func
import scipy
import numpy



#генерация простых чисел

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

# шаг 1
y = int(input('Введите y = '))
a = int(input('Введите a = '))
p = int(input('Введите p = '))

# количество простых чисел
t = int(input('Введите t = '))

#!!значения из примера
#y = 37
#a = 10
#p = 47
#t = 3
# список S простых чисел
S = [x for x in islice(prime_generator(), t)]

#eps = int(input('Введите небольшое целое число eps = '))
eps =1
# шаг 2

# разложение числа на простые множетели
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


# список степеней
k = list()

# матрица для поиска u на трерьем шаге
u_matrix = list()

# поиск степеней и гладкий чисел
i = 1
while len(k) < (t + eps):
    #вводим словарь для подсчета коэффициентов u для каждой строки, офк обнуляем его для каждой строки
    koef_u = dict()
    for j in S:
        koef_u[j] = 0
    # переводим в множества и делаем проверку на подмножество
    if set(Factor(one_way_func(a, i, p))) <= set(S):
        k.append(i)
        for j in Factor(one_way_func(a, i, p)):
            koef_u[j] += 1
        P = list()
        for g, v in koef_u.items():
            P.append(v)
        u_matrix += [P]
    i += 1

# шаг 3

# перевод списков левой и правой части системы в матрицу
u_matrix = numpy.array(u_matrix)
k_matrix = numpy.array(k)

print('Левая часть системы в матричном представлении:\n', u_matrix)
print('Правая часть системы в матричном представлении:\n', k_matrix)

#Вводим значения u,полученные в ходе решения системы
print('Введите решение системы уравненией:')
i = 1

# список для записи результатов системы уравнений
u_result = list()

while i <= t:
    u_result.append(int(input(f'Введите значение {i} переменной:\n')))
    i += 1

# шаг 4

r = 1

# словаь для записи частоты простого числа, на которые раскладывается гладкое число p_t
koef_p = list()

while r <= 5:
    # наше гладное число
    p_t = y * one_way_func(a, r, p) % p
    # гладкое число p_t раскладываем на простые и смотрим чтобы все они входили в S, для этого
    # переводим в множества и делаем проверку на подмножество
    if set(Factor(p_t)) <= set(S):
        # подсчитываем каждое простое число из которого состоит наше гладкое
        for l in S:
            h = 0
            while p_t % l == 0:
                h += 1
                p_t /= l
            koef_p.append(h)
        break
    r += 1


# шаг 5

i = 0
# запишем сюда результат

res = 0
# считаем значение "под суммой"
while i < t:
    res += koef_p[i] * u_result[i]
    i += 1
res -= r

x = (res % (p - 1))
print('Найденный x равен: ', x)

print('Проверка:', one_way_func(a, x, p))

""" НЕ РАБОТАЕТ!
Q, R = numpy.linalg.qr(u_matrix)
# решаем систему уравнений и находим u
x = scipy.linalg.solve_triangular(R, Q.T.dot(k_matrix), lower=False)
print(x)
from decimal import Decimal
print(Decimal(x[1]).as_integer_ratio())

a, b = x[1].as_integer_ratio()

print(a)
print(b)

from инверсия import inversia

c = inversia(p-1, b)
print(c)
print(c*a)
print((c*a)%(46))
"""



