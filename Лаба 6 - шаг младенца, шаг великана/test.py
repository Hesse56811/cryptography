"""
def stepen_po_mod(x,a,p):
    y=1
    a=a%p
    while x>0:
        if x&1:
            y=(y*a)%p
        x=x>>1
        a=(a*a)%p
    return y
def po_mod(a,p):
    po_mod=(p+(a%p))%p
    return po_mod



ryad1=[]
i=0
while i<(m-1):
    ryad1.append(po_mod((stepen_po_mod(i,a,p))*y,p))
    i=i+1
ryad2=[]
j=1
while j<k:
    ryad2.append(stepen_po_mod(j*m,a,p))
    j=j+1
print(ryad1)
print(ryad2)
"""