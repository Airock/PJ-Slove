bitmap=[0]*1000000
bitmap[1]=1 
bitmaplen=len(bitmap)
moni=2
maxdata=2
maxCount=2
while moni<bitmaplen: 
    count=0
    data=moni
    while data!=1:
        if data<bitmaplen:
            bitmap[data]=1
        if data%2==0:
            data/=2
        else:
            data=data*3+1
        count+=1
    if count>maxCount:
        maxCount=count
        maxdata=moni
    while moni<bitmaplen and bitmap[moni]==1:
        moni+=1
print maxdata
