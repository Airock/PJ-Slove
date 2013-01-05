def getBit(value):
    stage=0
    while value-(stage+1)*9*(10**stage)>0:
        value-=(stage+1)*9*(10**stage)
        stage+=1

    index=(value-1)/(stage+1)
    subindex=(value-1)%(stage+1)
    return int(str(index+10**stage)[subindex])

tot=1
for i in [10**i for i in range(7)]:
    tot*=getBit(i)
print tot
