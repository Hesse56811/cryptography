from one_way_alg import one_way_func
from инверсия import inversia
import sys

# вводим 2 больших простых числа и считаем еще 2 на основе их
P = int(input('Введите большое простое число P = '))
Q = int(input('Введите большое простое число Q = '))

N = P * Q

Fi = (P - 1) * (Q - 1)

print('Абонент вычислил число N = ', N)
print('Абонент вычислил число Fi = ', Fi)

d = int(input('Введите число d, взаимнопростое с Fi = '))

if d > Fi:
    print('d не может быть больше Fi')
    sys.exit()

c = inversia(Fi, d)
#print(c)

#ввод самого сообщения
m = input('Введите сообщение m = ')

#ввод значения хеш функции
y = int(input('Введите значение хеш-функции: '))

s = one_way_func(y, c, N)
print(s)

# часть для проверки подлинности

N = int(input('Введите открытый ключ N: '))
d = int(input('Введите открытый ключ d: '))

s = int(input('Введите цифровую подпись s: '))

print(one_way_func(s, d, N))







