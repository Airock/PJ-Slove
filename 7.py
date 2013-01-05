import math
def isPrim(num):
    if num == 2 or num == 3:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
count=0;
current=1;
while 1:
    current +=1
    if isPrim(current):
        count+=1
        if count == 10001:
            break;

print count
print current
