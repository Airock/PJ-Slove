#!/usr/bin/python
a=[0 for x in range(10000)]
for i in range(2,100):
    if a[i]==0:
        for j in range(i*2,10000,i):
            a[j]=1
d=dict()
for i in range(2,10000):
    if a[i]==0 and len(set(str(i)))>=3:
        s=list(str(i))
        s.sort()
        st=''
        st= st.join(s)
        if st in d:
            d[st].append(i)
        else:
            d[st]=[i]

for i in d:
    if len(d[i])>=3:
        d[i].sort
        #print d[i]
        for j in range(len(d[i])-2): 
            for k in range (max(2,j+2),len(d[i])):
                if (d[i][j]+d[i][k])/2 in d[i]:
                    print d[i][j]
                    print (d[i][j]+d[i][k])/2
                    print d[i][k]

