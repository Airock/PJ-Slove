def isPrim(value):
    if value==2 or value ==3:
        return True
    if value%2==0 or value%3==0:
        return False
    i=2
    while i*i<=value:
        if value%i==0:
            return False
        i++
    else:
        return  True
while True:

