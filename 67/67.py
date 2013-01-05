f=open("triangle.txt")
d=f.read()
data=d.split("\r\n")
data.pop()
for i in range(len(data)):
    data[i]=map(lambda x:int(x), [j for j in data[i].split()])
print data
for i in range(len(data)-2,-1,-1):
    for j in range(i+1):
        data[i][j]+=max(data[i+1][j],data[i+1][j+1])
print data[0][0]
