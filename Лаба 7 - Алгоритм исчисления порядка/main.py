from math import sqrt
from itertools import islice

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


y = int(input('Введите y = '))
a = int(input('Введите a = '))
p = int(input('Введите p = '))

# количество простых чисел
t = int(input('Введите t = '))

# список S простых чисел
S = [x for x in islice(prime_generator(), t)]

eps = int(input('Введите небольшое целое число eps = '))




