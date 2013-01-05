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
panlist=[]
for i in permute_in_place(range(1,10)):
    data=map(lambda x:str(x),i)
    for j in range(1,5):
        x=int(''.join(data[:j]))
        y=int(''.join(data[j:5]))
        z=int(''.join(data[5:]))
        if x*y==z and panlist.count(z)==0:
            panlist.append(z)
print reduce(lambda x,y:x+y, panlist)
