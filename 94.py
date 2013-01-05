#!/usr/bin/python
#assume the triangle have three edges, a,a a+/-1 then the perimeter will be 3a+/-1
#a will less/equal to 333,333,333

import math
total=0
a=3
def isSqNum(a):
    b = int(math.sqrt(a))
    if (b*b == a):
        return 1
    return 0 
while a<= 166666667:
    if isSqNum((a*2-1)**2-a**2):
        print "b: " + str(a*2) + " a: " + str(a*2-1) + " peri: " + str(a*6-2)
        total += (a*6-2)
        a*=2
    elif isSqNum((a*2+1)**2 - a**2):
        print "b: " + str(a*2) + " a: " + str(a*2+1) + " peri: " + str(a*6+2)
        total += (a*6+2)
        a*=2
    else:
        a+=1
    
print "Total:  "+str( total)


#while a <= 166666667: #333333333:
#    b2 = (a*2-1)**2 - a**2
#    b = int(math.sqrt(b2))
#    if (b*b == b2):
#        print "b: "+str(a*2) + " a: "+str(a*2-1)
#        print "perimter:" + str(a*6-2)
#        total = total + a*6-2
#        a*=2
#        continue
#    else:
#        b2= (a*2+1)**2-a**2
#        b=int(math.sqrt(b2))
#        if(b*b==b2):
#            print "b: " +str(a*2)+ " a: "+str(a*2+1)
#            print "perimeter:" + str(a*6+2)
#            total = total + a*6+2
#            a*=2
#            continue
#    a+=1
#
#    
#print "Total:  "+str( total)
#
