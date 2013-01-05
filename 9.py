for i in range(334,1001):
    for j in range((1000-i)/2,1000-i):
        if i**2==j**2+(1000-i-j)**2:
            print "i:"+str(i)+"j:"+str(j)+"k:"+str(1000-i-j)
            print i*j*(1000-i-j)
