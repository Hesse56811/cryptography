import math
import os
def stepen_po_mod(x,a,p):
    y=1
    a=a%p
    while x>0:
        if x&1:
            y=(y*a)%p
        x=x>>1
        a=(a*a)%p
    return y
Pb=int(input('Введите большое простое число Pb= '))
if Pb<1:
    print('Pb не может быть отрицательным или равным 0 ')
    os.system("pause")
Qb=int(input('Введите большое простое число Qb= '))
if Qb<1:
    print('Qb не может быть отрицательным или равным 0')
    os.system("pause")
Nb=Pb*Qb
F=(Pb-1)*(Qb-1)
db=int(input('Введите число db, взаимнопростое с F '))
if db>F:
    print('db не может быть больше F')
    os.system("pause")
Cb=int(input('Боб выбирает свое закрытое число Cb= '))
if Cb<1:
    print('Cb не может быть отрицательным или равным 0')
    os.system("pause")
m=int(input('Алиса передает сообщение m= '))
if m>Nb:
    print('m должно быть меньше Nb')
    os.system("pause")
e=stepen_po_mod(db,m,Nb)
mb=stepen_po_mod(Cb,e,Nb)
if m==mb:
    print('Информация передана успешно')
else:
    print('Условия не соблюдены')