lst=[1,2,5,10,20,50,100,200]
def getway(v,s):
    if v%s==0 :
        result=1
        rg=v/s
    else:
        result=0
        rg=v/s+1
    for i in range(rg):
        if s==2:
            result+=1
        else:
            result+=getway(v-s*i,lst[lst.index(s)-1])
    return result
print getway(200,100)+1
