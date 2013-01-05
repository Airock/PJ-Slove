cur=[1144066,23,10] #C23,10
def incN(input):
    value=input[:]
    value[1]+=1
    value[0]*=value[1]
    value[0]/=value[1]-value[2]
    return value
def decR(input):
    value=input[:]
    value[0]*=value[2]
    value[2]-=1
    value[0]/=value[1]-value[2]
    return value
count = 0
for i in range(23,101):
    while decR(cur)[0]>1000000:
        cur=decR(cur)
        print cur
    count+=cur[1]-(cur[2]-1)*2-1
    cur = incN(cur)
print count
    
