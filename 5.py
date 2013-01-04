def mincm(a, b):
    if a > b:
        return mincm(b,a)
    if a == 0:
        return b
    else:
        return mincm(b % a, a)

def maxcm(a,b):
    mincm_rslt = mincm(a,b)
    return (a*b/mincm_rslt)

print reduce(maxcm,[x for x in range(20,9,-1)])
