ifile=open("matrix.txt")
input=ifile.read()
array=input.split("\n")
for i in range(80):
    tmp=array[i].split(",")
    for j in range(len(tmp)):
        tmp[j]=int(tmp[j])
    array[i]=tmp
#array=[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

size=len(array)

def getMaxB(array,i,j,dir): #True for down False for up
    if i == 0 or i == size-1:
        return array[i][j]+array[i][j+1]
    else:
        return array[i][j]+min(array[i][j+1],getMaxB(array,i+1 if dir else i-1,j,dir))

def getMax(array,i,j):
    if i == 0:
        return array[i][j]+min(array[i][j+1],getMaxB(array,i+1,j,True))
    elif i==size-1: 
        return array[i][j]+min(array[i][j+1],getMaxB(array,i-1,j,False))
    else:
        return array[i][j]+min(array[i][j+1],getMaxB(array,i+1,j,True),getMaxB(array,i-1,j,False))

tmp=[0]*size
for j in range(size-2,0,-1):
    for i in range(size):
        tmp[i]=getMax(array,i,j)
    for i in range(size):
        array[i][j]=tmp[i]
for i in range(size):
    array[i][0]+=array[i][1]

result=array[0][0]
for i in range(1,size):
    if array[i][0]<result:
        result=array[i][0]
print result

