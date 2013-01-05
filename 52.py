def sortData(value):
    lst=list(str(value))
    lst.sort()
    return int(''.join(lst))

data=1
while True:
    sd=sortData(data)
    for i in range(2,7):
        if sortData(data*i)!=sd:
            break
    else:
        print data
        break    
    data+=1
