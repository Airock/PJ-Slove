def getBinaryString(value):
    result=''
    while value>0:
        result=str(value%2)+result
        value/=2
    return result
#solution 1:
data=1
sum=0
while data<1000000:
    if not cmp(data, int(str(data)[::-1])) and \
            not cmp(getBinaryString(data),getBinaryString(data)[::-1]):
        sum+=data
    data+=1
print sum
#solution 2:
print reduce(lambda x,y:x+y, \
        filter(lambda x: not cmp(x,int(str(x)[::-1])) and not \
        cmp(getBinaryString(x),getBinaryString(x)[::-1]), \
        range(1,1000000)))
