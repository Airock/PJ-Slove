def gcd(a,b):
    if a<b:
        return gcd(b,a)
    if b == 0:
        return a
    return gcd(a%b,b)

def gcd2(a,b):
    if a<b:
        a,b=b,a
    while b!=1:
        if b == 0:
            return a
        else:
            a,b=b,a%b
    return 1

x=1
y=2
j=0
for i in range(1000):
    j+=len(str(x+y))-len(str(y))
    x,y = y,(y*2+x)
print j