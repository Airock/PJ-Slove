ifile=open("matrix.txt")
input=ifile.read()
array=input.split("\n")
size=80
for i in range(size):
    tmp=array[i].split(",")
    for j in range(len(tmp)):
        tmp[j]=int(tmp[j])
    array[i]=tmp
size=len(array[0])

for i in range(1,size*2-1):
    x=max(0,i-size+1)
    y=min(i-size+1,0)+size-1
    for j in range(size-abs(i-size+1)):
        if x-1<0:
            array[x][y]+=array[x][y-1]
        elif y-1<0:
            array[x][y]+=array[x-1][y]
        else:
            array[x][y]+=min(array[x-1][y],array[x][y-1])
        x+=1
        y-=1

print array[size-1][size-1] 
