f=open("triangles.txt")
data=f.read()
array=data.split("\n")
array.pop()
count=0
for i in array:
    tr=i.split(",")
    for j in range(len(tr)):
        tr[j]=int(tr[j])
    axb=(tr[0]*tr[3]-tr[2]*tr[1])
    bxc=(tr[2]*tr[5]-tr[4]*tr[3])
    cxa=(tr[4]*tr[1]-tr[0]*tr[5])
    if axb*bxc>0 and bxc*cxa>0:
        count+=1

print count
