import sys
from one_way_alg import one_way_func

m = int(input('Введите число m = '))
if m < 1:
    print('m не может быть отрицательным или равным 0')
    sys.exit()

k = int(input('Введите число k = '))
if k < 1:
    print('k не может быть отрицательным или равным 0')
    sys.exit()

p = int(input('Введите число p = '))
if p > m * k:
    print('p должно быть меньше, чем произведение чисел m и k')
    sys.exit()

a = int(input('Введите число a = '))
if a < 1:
    print('a не может быть отрицательным или равным 0')
    sys.exit()

y = int(input('Введите число y = '))
if y < 1:
    print('y не может быть отрицательным или равным 0')
    sys.exit()

g = m
h = False

while g < (k * m):
    if h:
        break
    a_step = one_way_func(a, g, p)
    for step in range(m - 1):
        if (one_way_func(a, step, p) * y % p) == a_step:
            im = g
            j = step
            h = True
            break
        if (one_way_func(a, step, p) * y % p) > a_step:
            break
    g += 1


print(im - j)

print("проверка: ", one_way_func(a, im - j, p))
