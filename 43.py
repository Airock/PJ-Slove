import string
def permute_in_place(a):
    a.sort()
    yield list(a)

    if len(a) <= 1:
        return

    first = 0
    last = len(a)
    while 1:
        i = last - 1

        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i] # swap the values
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == first:
                a.reverse()
                return
divList=[2,3,5,7,11,13,17]
divList=[7,11,13,17]
lst=map(lambda x:str(x),range(10))
sum=0
for i in permute_in_place(lst):
    data=''.join(i)
    if int(data[3])%2==1 or (int(data[2])+int(data[3])+int(data[4]))%3!=0 or (data[5] != '0' and data[5]!='5'):
        continue
    for i in range(len(divList)):
        if string.atoi(data[i+4:i+7],10)%divList[i] != 0:
            break
    else:
        sum+=int(data)
        print data
print sum 
    
