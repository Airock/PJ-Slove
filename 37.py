bitmap=[1]*1000000 #consider first 1000000 numbers
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

data=11
sum=0
count=0
while data<len(bitmap):
    if bitmap[data]==1:
        for i in range(1,len(str(data))):
            if bitmap[int(str(data)[:-i])]==0:
                break;
            if bitmap[int(str(data)[i:])]==0:
                break;
        else:
            print data
            sum+=data
            count+=1
            if count==11:
                print "finish"
                break
    data+=1
print sum 
