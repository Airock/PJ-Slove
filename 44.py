bitmap=[0]*10000000
pent=lambda x:x*(x*3-1)/2

i=1
while pent(i)<len(bitmap):
    bitmap[pent(i)]=1
    i+=1

i=1
found=False
while i<len(bitmap) and found==False:
    sub=pent(i)
    j=1
    first=pent(j)
    while (pent(j+1)-first) < sub and first*2+sub<len(bitmap):
        if bitmap[first+sub] == 1 and bitmap[first*2+sub] == 1:
            found=True
            print "a:"+str(first)+" b:"+str(first+sub)+ " D:"+ str(sub)
            break
        else:
            j+=1
            first=pent(j)
    i+=1
