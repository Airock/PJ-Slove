import math
y=10**12
x= int(math.sqrt(10**12*(10**12-1)/2))
print 10**12*(10**12-1)/2
x+=1

while  cmp(x*(x-1)*2, y*(y-1)):
    if x*(x-1)*2<y*(y-1):
        x+=1
    else:
        y+=1
print x
