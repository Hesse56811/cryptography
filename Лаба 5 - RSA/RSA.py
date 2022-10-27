from one_way_alg import one_way_func
from инверсия import inversia
import sys

m = int(input('Введите сообщение m = '))

P = int(input('Введите большое простое число P = '))
Q = int(input('Введите большое простое число Q = '))

N = P * Q

print('Абонент вычислил число N = ', N)

Fi = (P - 1) * (Q - 1)
print('Абонент вычислил число Fi = ', Fi)

d = int(input('Введите число d, взаимнопростое с Fi = '))
if d > Fi:
    print('d не может быть больше Fi')
    sys.exit()

с = inversia(Fi, d)
print("Секретный ключ c = ", с)

#кодируем сообщение
e = one_way_func(m, d, N)

print('Зашифровонное сообщение e = ', e)

# разкодируем сообщение
m_p = one_way_func(e, с, N)
print('Расшифрованное сообщение m = ', m_p)


