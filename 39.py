#X=P^2+PQ
#Y=Q^2/2+PQ
#Z=P^2+Q^2/2+PQ
#sum(X,Y,Z)=3PQ+Q^2+2P^2
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=1:
        if b == 0:
            return a
        else:
            a,b=b,a%b
    return 1
triple=[]
sum=[]
for p in range(1,22):
    for q in range(1,31):
        if q%2==1:
            continue
        x=p**2+p*q
        y=q**2/2+p*q
        z=p**2+q**2/2+p*q
        g= gcd(x,gcd(y,z))
        x/=g
        y/=g
        z/=g
        if triple.count([x,y,z])==0:
            triple.append([x,y,z])
            sum.append(x+y+z)
maxcount=0
maxindex=0
for i in range(1,1001):
    count=0
    for j in sum:
        if i%j==0:
            count+=1
    if count>maxcount:
        maxcount=count
        maxindex=i
print maxcount
print maxindex

