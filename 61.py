array=[[],[],[],[],[],[]]
i=1
while i*(i+1)/2 <10000:
    if i*(i+1)/2 >999:
        array[0].append(i*(i+1)/2)
    i+=1
print len(array[0])
i=1    
while i*i <10000:
    if i*i >999:
        array[1].append(i*(i+1)/2)
    i+=1
print len(array[1])
i=1    
while i*(3*i-1)/2 <10000:
    if i*(3*i-1)/2 >999:
        array[2].append(i*(i+1)/2)
    i+=1
print len(array[2])
i=1    
while i*(i*2-1) <10000:
    if i*(i*2-1) >999:
        array[3].append(i*(i+1)/2)
    i+=1
print len(array[3])
i=1    
while i*(i*5-3)/2 <10000:
    if i*(i*5-3)/2 >999:
        array[4].append(i*(i+1)/2)
    i+=1
print len(array[4])
i=1    
while i*(3*i-2) <10000:
    if i*(i*3-2) >999:
        array[5].append(i*(i+1)/2)
    i+=1
print len(array[5])

bitmap=[0]*100
bitmap2=[[[0]*2]*100]*6

for i in range(6):
    for j in array[i]:
        #bitmap[j%100]+=1
        #bitmap[j/100]+=1
        print j
        bitmap2[i][j%100][1]+=1
        bitmap2[i][j/100][0]+=1

print bitmap2
        
