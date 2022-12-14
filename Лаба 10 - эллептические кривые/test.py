import math

a=int(input('Введите значение а='))
b=int(input('Введите значение b='))
p=int(input('Введите простое число р='))

def evklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = evklid(b % a, a)
        return (g, x - (b // a) * y, y)

def invers_po_mod(a, p):
    g, x, y = evklid(a, p)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x%p

def po_mod(a,p):
    po_mod=(p+(a%p))%p
    return po_mod

def stepen_po_mod(x,y,p):
    res=1
    x=x%p
    while y>0:
        if y&1:
            res=(res*x)%p
        y=y>>1
        x=(x*x)%p
    return res


#Функция проверки кривой на сингулярность
def proverka(a,b):
    Uslovie=(4*(stepen_po_mod(a,3,p))+27*(stepen_po_mod(b,2,p)))
    if Uslovie==0:
        print('Данная кривая сингулярна и не может быть рассмотрена')
    else:
        print('Данная кривая несингулярна')

D=proverka(a,b)
X=int(input('Введите начальную координату х для эллиптической кривой вида [Y^2=X^3+a*X+b] ='))


#Найдем координаты точек и композиции точек
Y1=po_mod((stepen_po_mod(X,3,p)+a*X+b),p)
Y2=invers_po_mod(Y1,p)
K=po_mod((3*stepen_po_mod(X,2,p)+a)*invers_po_mod(2*Y1, p),p)
Xk=po_mod((K-2*X),p)
Yk=po_mod((K*(X-Xk)-Y1),p)
K1=po_mod(po_mod((Yk-Y1),p)*invers_po_mod(po_mod((Xk-X),p),p),p)
Xk1=po_mod((stepen_po_mod(K1,2,p)-X-Xk),p)
Yk1=po_mod((K1*(X-K1)-Y1),p)
print('Найдена первая точка с координатами: [',X,Y1,']')
print('Найдена вторая точка с координатами: [',X,Y2,']')
print('Найдена 1-ая композиция точек с координатами: [',Xk,Yk,']')
print('Найдена 2-ая композиция точек с координатами: [',Xk1,Yk1,']')
