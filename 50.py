#!/usr/bin/python
a=[0 for x in range(1000000)]
for i in range(2,1000):
    if a[i]==0:
        for j in range(i*2,1000000,i):
            a[j]=1
l=[]
for i in range(2, 1000000):
    if a[i] == 0:
        l.append(i)
biggest=0
lenth=0
for i in range(len(l)-10):
    j=i
    sum=0
    while sum<1000000:
        if j == len(l)-10:
            break;
        sum+=l[j]
        j+=1
        if sum in l and j-i>lenth:
            lenth = j-i
            biggest = sum
            print "len " + str(lenth)
            print "biggest: " + str(biggest)
    if len(l)-i < lenth:
        break;
print biggest
