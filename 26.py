data=2
rCount=0
for i in range(2,1000):
    d=1
    result=[]
    count=0
    while result.count(d)==0:
        result.append(d)
        d*=10
        d%=i
    
    if len(result)-result.index(d)>rCount:
        rCount=len(result)-result.index(d)
        data=i
print data        
