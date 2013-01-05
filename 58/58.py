from __future__ import division
def isPrim(a):
    for i in range(2,a-1):
        if a%i==0:
            return False
    return True

prim=0
nonprim=1
level=1
data=1
rat=2
num=4
#too slow
while True:
    for i in range(num):
        data+=rat
        if isPrim(data):
            prim+=1
        else:
            nonprim+=1
    rat+=2
    level+=1
    if level%10==0:
        print data
        print prim/(prim+nonprim)
    if prim/(prim+nonprim)<0.1:
        break
print level*2-1


