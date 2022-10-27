import os
import math
def stepen_po_mod(x,a,p):
    y=1
    a=a%p
    while x>0:
        if x&1:
            y=(y*a)%p
        x=x>>1
        a=(a*a)%p
    return y
import math
g=int(input('Введите кодообразующее число g= '))
if g<1:
    print('G не может быть отрицательным или равным 0')
    os.system("pause")
p=int(input('Введите кодообразующее число p= '))
if p<1:
    print('P не может быть отрицательным или равным 0')
    os.system("pause")
Xa=int(input('Введите секретный ключ абонента А= '))
if Xa<1:
    print('Xb не может быть отрицательным или равным 0')
    os.system("pause")
Xb=int(input('Введите секретный ключ абонента B= '))
if Xb<1:
    print('Xb не может быть отрицательным или равным 0')
    os.system("pause")
Ya=stepen_po_mod(Xa,g,p)
Yb=stepen_po_mod(Xb,g,p)
print('Открытый ключ абонента А= ', Ya)
print('Открытый ключ абонента B= ', Yb)
Zab=stepen_po_mod(Xa,Yb,p)
Zba=stepen_po_mod(Xb,Ya,p)
print(Zab)
print(Zba)
if Zab==Zba:
    print('Ключи совпали')
print('Секретный ключ шифрования равен ', Zab)
