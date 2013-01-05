bitmap=[1]*100000 #consider first 100000 numbers
bitmap[0]=0
bitmap[1]=0
data=2
while data<len(bitmap):
    if bitmap[data]==1:
        i=data*2
        while i<len(bitmap):
            bitmap[i]=0
            i+=data
    data+=1

pair=(0,0,0)
for a in range(-999,1000):
    for b in range(-999,1000):
        n=0
        while bitmap[n*n+a*n+b]:
            n+=1
        if n > pair[0]:
            pair=(n,a,b)
            
print pair
