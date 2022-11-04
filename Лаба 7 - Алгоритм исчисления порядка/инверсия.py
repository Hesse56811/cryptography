from Евклид import alg_evklid


def inversia(m, c):
    return (alg_evklid(m, c)[2]) % m


if __name__ == "__main__":
    m = int(input('Введите модуль, m = '))
    c = int(input('Введите число, c = '))
    d = alg_evklid(m, c)[2]
    print('Инверсия = ', d % m)






