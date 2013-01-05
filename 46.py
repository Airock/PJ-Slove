import math
bitmap=[1]*100000 #find within 100000
tsrange=int(math.sqrt(len(bitmap)/2))
ts=map(lambda i:i**2*2, [x for x in range(tsrange)])
for i in range(2,len(bitmap)):
    if bitmap[i]==1:
        j=i+i
        while j<len(bitmap):
            bitmap[j]=0
            j+=i
    else:
        i+=1


value=3
while value<len(bitmap):
    if bitmap[value]==0:
        found=False
        for i in ts:
            if i >= value:
                break;
            if bitmap[value-i]==1:
                found=True
                break;
        if found==False:
            print value
            break
    
    value+=2
