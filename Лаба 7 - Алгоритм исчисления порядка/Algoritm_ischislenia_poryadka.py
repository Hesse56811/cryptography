import os 
import math
from collections import Counter


def disklog(g,a,p):
    i=1
    while i>0:
        print ('(g**i)%p=',(g**i)%p,'g',g,'i',i,'a', a)
        if (g**i)%p==a:
            break
        i=i+1
    return i
        
        

def primefacs(n):
    i=2
    primefac=[]
    while i*i<=n:
        while n%i==0:
            primefac.append(i)
            n=n/i
        i=i+1
    if n>1:
        primefac.append(n)
    return primefac

def smoothcheck(n,p):
    maximum=-1
    while (not(n%2)):
        maximum=max(maximum,2)
        n=int(n/2)
    for i in range (3,int(math.sqrt(n)),2):
        while (n%i==0):
            maximum=max(maximum,i)
            n=int(n/i)
    if (n>2):
        maximum=max(maximum,n)
    return(maximum<=p)



def is_prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0 and x!=1:
            return 0
        return 1

def foo(n):
    pros=[2,3]
    i=1
    k=2
    while k<n:
        if is_prime(i)==1:
            pros.append(i)
            k=k+1
        i=i+1   
    print(pros[:N])
    return pros[:N]
N=int(input('Количество необходимых простых чисел:'))
foo(N)
a=int(input('Введите число а:'))
p=int(input('Введите число p:'))
y=int(input('Введите число y:'))
s=foo(N)
t=int(input('Необходимое количество гладких чисел:'))
k=1
findes=0
while findes<t:
    if(smoothcheck((a**k)%p,s[N-1])):
        findes=findes+1
        print('Разложение при k=',k,primefacs((a**k)%p))
    k=k+1

#находим r
r=1
findes=0
while findes<1:
    if(smoothcheck(y*(a**r)%p,s[N-1])):
        findes=findes+1
        print('Разложение при подходящем r:',primefacs(y*(a**r)%p))
        break
    r=r+1
print('Подходящий r=' ,r)
c=Counter(primefacs(y*(a**r)%p))
x=0
i=2
while i<=N-1:
    print('wasd',a,i,p-1)
    x=x+c[i] * disklog(a,i,p-1)
    print(disklog(a,i,p-1))
    print(c[i])
    print(x)
    i=i+1
x=(x-r)%(p-1)
print('Решение:',x)
    
print ('Если брать как в классе при 30 тоже решается, тк остаток тоже 2 , из-за того что у системы уравнений несколько решений(10**30)%46:'(10**30)%46)