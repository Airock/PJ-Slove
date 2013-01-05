'''
slution one: recuresive
def rec(x,y):
    if x==0 or y==0:
        return 1
    return rec(x-1,y)+rec(x,y-1)

for i in range(1,21):
    print rec(i,i) '''
""" a more simple way to slove this problem is : C(20)(40)"""
col=20
grid=col+1
a=[0]*(grid+2)
a[1]=1
for i in range(0,grid-1):
    b=[0]*(grid+2)
    for j in range(1,i+3):
        b[j]=a[j]+a[j-1]
    a=b[:]
    print b        

for i in range(grid-1,0,-1):
    b=[0]*(grid+2)
    for j in range(i,0,-1):
        b[j]=a[j]+a[j+1]
    a=b[:]
    print b
print a[1]
