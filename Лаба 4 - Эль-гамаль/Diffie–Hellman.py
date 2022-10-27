from one_way_alg import *


g = int(input('Введите g '))
p = int(input('Введите p '))
Xa = int(input('Введите секретный ключ абонента А '))
Xb = int(input('Введите секретный ключ абонента B '))


Ya = one_way_func(g, Xa, p)
Yb = one_way_func(g, Xb, p)

print('Открытый ключ абонента А ', Ya)

print('Открытый ключ абонента B ', Yb)

Zab = one_way_func(Yb, Xa, p)

Zba = one_way_func(Ya, Xb, p)

print('Zab = ', Zab)
print('Zba = ', Zba)

# 5 23 7 13 10