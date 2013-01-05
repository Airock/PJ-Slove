def getPF(value):
    pf=2
    num=0
    while value>1:
        if value%pf==0:
            num+=1
            while value%pf==0:
                value/=pf
        else:
            pf+=1
    return num

i=2
flag=False
while flag==False:
    for i in range(4):
        if getPF(i)!=4:
            i+=1
            break;
        elif i == 3:
            flag=True
            break;
print i
        
