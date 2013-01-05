max=2540160 #9!*7
def fac(value):
    if value==0:
        return 1
    return reduce(lambda x,y:x*y,[i for i in range(1,value+1)])
bitmap=map(fac,range(1,10))
bitmap.insert(0,1)
def getFac(value):
    tot=0
    for i in [int(i) for i in str(value)]:
        tot+= bitmap[i]
    return tot

for i in range(3,max):
    if getFac(i)==i:
        print i

