from Евклид import alg_evklid

m = int(input('Введите модуль, m = '))
c = int(input('Введите число, c = '))

d = alg_evklid(m, c)[0]

print('Инверсия = ', d % m)




