count=0
for i in range(1,51*51):
    for j in range(i,51*51):
        if i==j:
            continue
        xi,yi=i%51,i/51
        xj,yj=j%51,j/51
        arr=[xi**2+yi**2,xj**2+yj**2,(xi-xj)**2+(yi-yj)**2]
        arr.sort()
        if arr[0]+arr[1]==arr[2]:
            count+=1
print count
