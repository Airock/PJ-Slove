file=open("words.txt")
input=file.read()
wordArray=input.split(",")
for i in range(len(wordArray)):
    word=wordArray[i].strip('"')
    sortWord=list(word)
    sortWord.sort()
    wordArray[i]=[''.join(sortWord),word]

wordArray.sort(lambda x,y:cmp(x[0],y[0]))
for i in range(len(wordArray)-1):
    if not cmp(wordArray[i][0],wordArray[i+1][0]):
        print wordArray[i]
        print wordArray[i+1]
i=1
while i*i<1000000000:
    i+=1
sqrArray=[0]*i
for j in range(i):
    num=str(j*j)
    sortNum=list(num)
    sortNum.sort()
    sqrArray[j]=[''.join(sortNum),num]

sqrArray.sort(lambda x,y:cmp(x[0],y[0]))
newArray=[]
for i in range(len(sqrArray)-1):
    if not cmp(sqrArray[i][0],sqrArray[i+1][0]):
        dup=0
        for j in range(len(sqrArray[i][0])-1):
            if not cmp(sqrArray[i][0][j],sqrArray[i][0][j+1]):
                dup+=1
        
        if dup<2:
            newArray.append(sqrArray[i])

newArray.sort(lambda x,y:cmp(len(x[1]),len(y[1])))
for i in newArray:
    print i
