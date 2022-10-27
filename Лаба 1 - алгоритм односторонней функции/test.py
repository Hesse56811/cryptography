import os, sys
import math

a=int(input('Введите значение a='))
p=int(input('Введите значение p='))
x=int(input('Введите значение x='))
def stepen_po_mod(x,a,p):
    y=1
    a=a%p
    while x>0:
        if x&1:
            y=(y*a)%p
        x=x>>1
        a=(a*a)%p
    return y
y=stepen_po_mod(x,a,p)
print(y)



