tria=lambda n:n*(n+1)/2
pent=lambda n:n*(n*3-1)/2
hexa=lambda n:n*(n*2-1)

level=0
bitmapsize=10000000
index=[286,166,144]
funMat=[tria,pent,hexa]
for i in range(3):
    while funMat[i](index[i])<level*bitmapsize:
        index[i]+=1

found=False
while found==False:
    bitmap=[0]*bitmapsize
    for i in range(3):
        while funMat[i](index[i])<(level+1)*bitmapsize:
            num=funMat[i](index[i])
            bitmap[num-level*bitmapsize]+=1
            if i==2 and bitmap[num-level*bitmapsize]==3:
                print num
                found=True
                break
            index[i]+=1
    level+=1

