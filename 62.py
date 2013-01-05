def getBase(value):
    currentBase=2
    while currentBase**3!=value:
        if currentBase**3>value:
            currentBase=currentBase*3/4
        else:
            currentBase*=2
    return currentBase

def getPerm(value):



startvalue = 345
currentTube=345**3
while getPerm(currentTube)<5:
    startvalue+=1
    currentTube=startvalue**3

