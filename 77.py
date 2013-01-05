#!/usr/bin/python

a=[0 for x in range(10000)]
for i in range(2,100):
    if a[i]==0:
        for j in range(i*2,10000,i):
            a[j]=1

def cal(num, min,level):
    #print str(level)+"num: " + str(num) + " min:" + str(min)
    if min < 2 :
        return 0
    if a[num] == 0:
        init=1
    else :
        init=0


    for i in range(min, num/2+1):
        if a[i]==0:
            init+= cal(num-i,i,level+1)
    return init

def find(start,end,value):
    #print "start:" +str(start) + " end:" + str(end) 
    if start>=end:
        return -1
    if start+1==end:
        return end 
    if cal((start+end)/2,2,0)>value:
        return find(start, (start+end)/2,value)
    else:
        return find((start+end)/2,end,value)
print find(2,100,5000)
