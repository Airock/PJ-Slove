length=28123
bitmap=[0]*(length+1)
abanlist=[]
for data in range(1,length+1):
    s=2
    sum=1
    while s*s<data:
        if data%s==0:
            sum+=data/s
            sum+=s
        s+=1
    if s*s==data:
        sum+=s
    if sum>data:
        abanlist.append(data)
abanlen=len(abanlist)
for k in [abanlist[i]+abanlist[j] for i in range(abanlen) for j in range(i,abanlen) \
        if abanlist[i]+abanlist[j]<length+1]:
    bitmap[k]=1
print reduce(lambda x,y:x+y,filter(lambda x:not bitmap[x],[x for x in range(length+1)]))

