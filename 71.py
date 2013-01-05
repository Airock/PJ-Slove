from __future__ import division
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
oldND=(0,1)
for d in range(8,1000001):
    if int(oldND[0]*d/oldND[1]) >= int(3*d/7):
        continue
    for n in range (int(3*d/7),int(oldND[0]*d/oldND[1]),-1):
        if gcd(d,n)==1:
            oldND=(n,d)
            continue
print oldND
