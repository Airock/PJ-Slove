f=open("keylog.txt")
d=f.read()
d=d.split("\n")
d.pop()
d.sort()
length=3*len(d)
all=set()
first=set()
while length>0:
    for i in d:
        if len(i)>=1:
            first.add(i[0])
        if len(i)>=2:
            all.add(i[1])
        if len(i)=3:
            all.add(i[2])
        for i in first:
            if i in all:
                continue
        else:

