left=1
result=[]
while left*left<987654321:
    bitmap=[0]*10
    right=1
    fail=False
    while fail==False:
        prod=left*right
        for i in str(prod):
            bitmap[int(i)]+=1
            if i=='0' or bitmap[int(i)]>1:
                fail=True
                break
        if fail== False and bitmap.count(0)==1:
            #print "left:"+str(left)
            #print "right:"+str(right)
            output=""
            for i in range(right):
                output+=str(left*(i+1))
            #print output
            result.append(int(output))
        right+=1
    left+=1
result.sort()
print result
