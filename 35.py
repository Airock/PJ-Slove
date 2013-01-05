bitmap=[1]*1000000 #consider first 1000000 numbers
bitmap[0]=0
bitmap[1]=0
data=2
while data*data<len(bitmap):
    if bitmap[data]==1:
        i=data*2
        while i<len(bitmap):
            bitmap[i]=0
            i+=data
    data+=1

count=4
data=11
while data<len(bitmap):
    dstr=str(data)
    for i in range(len(dstr)-1):
        dstr=dstr[1:]+dstr[0]
        if bitmap[int(dstr)]==0:
            break
    else:
        count+=1 
    data+=1
    while data<len(bitmap) and bitmap[data]==0:
        data+=1
print count

