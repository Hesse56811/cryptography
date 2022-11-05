import math



def alg_evklid(a, b):

    u = [a, 1, 0]
    v = [b, 0, 1]

    while v[0] != 0:
        q = math.floor(u[0]/v[0])
        T = [u[0] % v[0], u[1] - q * v[1], u[2] - q * v[2]]
        u = v
        v = T
    return u


if __name__ == '__main__':
    a = int(input("Введидите первый коэффициент, а = "))
    b = int(input("Введите второй коэффициент, b = "))
    alg_evklid(a, b)
    print('gcd(a,b) = ', alg_evklid(a, b)[0])
    print('x = ', alg_evklid(a, b)[1])
    print('y = ', alg_evklid(a, b)[2])



