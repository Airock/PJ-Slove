data=1000000
array=map(lambda z:reduce(lambda x,y:x*y,range(1,z)),range(2,11))
array[0:0]=[1]
print array
result=""
bitset=range(0,10)
while len(bitset)>0:
    num=(data-1)/array[len(bitset)-1]
    data-=num*array[len(bitset)-1]
    result+=str(bitset[num])
    bitset.remove(bitset[num])
print result
