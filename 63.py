i=1
count=0
while 9**i>=10**(i-1):
    j=9
    while j**i>=10**(i-1):
        j-=1
    count+=9-j
    i+=1
print count 
