import math

a = 1
x = 1
p = 1


def one_way_func(a, x, p):
    y = 1
    bin_x = str(bin(x))[2:][::-1]
    ost = a % p
    for k in bin_x:
        if k == '1':
            y = (y * ost) % p
        ost = (ost * ost) % p
    return y


if __name__ == "__main__":
    a = int(input("Введите a "))
    x = int(input("Введите x "))
    p = int(input("Введите p "))

    print(one_way_func(a, x, p))
# в примере a=3 x=100 p=7 ответ 4