array=filter(lambda x:x==int(str(x)[::-1]), [x*y for x in range(100,1000) for y in range(100,1000)]) 
max=0
for i in array:
    if i>max:
        max=i
print max

