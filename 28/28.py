def cal(a,b,c):
    total=a+b+c
    for i in range(1002/2-3):
        total+=3*c-3*b+a
        a,b,c=b,c,3*c-3*b+a
    return total
#print cal(1,3,13)+cal(1,9,25)+cal(1,7,21)+cal(1,5,17)-3

def cal(a,b):
    total=0
    for i in range(1002/2-1):
        total+=b
        a,b=b,2*b-a+8
    return total
print cal(1,3)+cal(1,9)+cal(1,7)+cal(1,5)+1