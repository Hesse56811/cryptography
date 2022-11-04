import numpy # импортируем библиотеку

M2 = numpy.array([[1., 0., 1., 0 ], [1., 1., 0., 0], [2., 2., 0. ,0 ], [0., 2., 1., 0]]) # Матрица (левая часть системы)
v2 = numpy.array([1., 2., 4., 7.]) # Вектор (правая часть системы)



print(M2)
print(v2)
#numpy.linalg.solve(M2, v2)

print(numpy.linalg.solve(M2, v2))

#v2 = numpy.vstack((v2, [1., 2., 4., 7.]))

#print(v2)
"""

#строки
m = 4
#столбцы
n = 3

A = np.random.randn(m, n)
b = np.random.randn(m)

A = np.array([[1, 0, 1], [1, 1, 0], [2, 2, 0], [0, 2, 1]])
b = np.array([1, 2,4, 7])

print(A)
print(b)

Q, R = la.qr(A)

print(Q.shape)
print(R.shape)

x = spla.solve_triangular(R, Q.T.dot(b), lower=False)
print(x)

la.norm(A.dot(x)-b, 2)

la.norm(R.dot(x) - Q.T.dot(b))

Q2, R2 = la.qr(A, mode="complete")

x2 = spla.solve_triangular(R[:n], Q.T[:n].dot(b), lower=False)

la.norm(A.dot(x)-b, 2)

la.norm(R2.dot(x2) - Q2.T.dot(b))

print(x - x2)

x3 = la.solve(A.T.dot(A), A.T.dot(b))

print(x3 - x)
"""
