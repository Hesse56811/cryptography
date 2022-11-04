import copy, numpy

a = numpy.array([[1., 0., 1.,1],
                 [1., 1., 0.,2],
                 [2., 2., 0.,4],
                 [0., 2., 1.,7]
                 ])
print(a)


def gaussFunc(a):  # В метод передавайте вещественный массив))
    eps = 1e-16

    c = numpy.array(a)  # с нам еще понадобится
    a = numpy.array(a)  # создаем копию массива a, используя библиотеку NumPy
    # (зачем? Python-язык с динамической типизацией,
    # приходящий а-любой объект, а мы должны попытаться кастануть его в массив )

    len1 = len(a[:, 0])  # хранит размер матрицы A, то есть n
    len2 = len(a[0, :])  # n+1
    # vectB = copy.deepcopy(a[:, len1])#вектор B в Ax=B

    for g in range(len1):

        max = abs(a[g][g])  # переменная для сохранения
        my = g  # максимума в текущем столбце
        t1 = g  # g
        while t1 < len1:  # цикл поиска максимума в столбце g
            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(max) < eps:  # Если найденный максимум < 0(машинного) выбрасываем ошибку
            raise DetermExeption("Check determinant")  # тк определитель матрицы равен нулю

        if my != g:
            a[g][:], a[my][:] = a[my][:], a[g][:]  # меняем текущую строку со строкой, в которой
            # максимум (красивая реализация swap(), да?)

        amain = float(a[g][g])  # коэффицент перед текущим x на диагонали

        z = g
        while z < len2:  # делим всю строку на amain коэффицент перед текущим
            a[g][z] = a[g][z] / amain  # x становится  1
            z += 1
        j = g + 1

        while j < len1:  # отнимаем строку, умноженную на коэффицент
            b = a[j][g]  # от следующей, в результате получаем столбец нулей.
            z = g  # Глобальный цикл выполняется до тех пор, пока
            while z < len2:  # не получатся нули в нижней треугольной матрице
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1

    a = backTrace(a, len1)  # обратный ход метода Гаусса

    print("Погрешность:")
    print(vectorN(c, a, len1))  # вывод нормы вектора невязки
    return a


class DetermExeption(Exception):  # Ошибка, проверьте определитель матрицы
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def backTrace(a, len1):  # обратный ход
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]


def vectorN(c, a, len1):  # c-начальная матрица a-ответ len1-кол столбцов, vectB-вектор B
    c = numpy.array(c)
    a = numpy.array(a)
    vectB = copy.deepcopy(c[:, len1])
    b = numpy.zeros((len1))
    i = 0

    while i < len1:  # подставляем полученные x-ы, в матрицу, получаем вектор невязки
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]
            j += 1
        i = i + 1

    c = copy.deepcopy(b)

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])  # отнимаем от вектора невязки вектор B
        # получаем норму
    return c


b = gaussFunc(a)
print("Ответ:")
print(b)