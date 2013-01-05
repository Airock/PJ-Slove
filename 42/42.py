f=open("words.txt")
names=f.read().split(",")
maxlen=len( reduce(lambda x,y:x if len(x)>len(y) else y,names))
i=1
triset=set()
while i*(i+1)/2  <maxlen*26:
    triset.add(i*(i+1)/2)
    i+=1
total=0
for i in names:
    num=sum(ord(j)-ord('A')+1 for j in i.strip('"'))
    set1=set()
    set1.add(num)
    if set1<triset:
        total+=1
print total


