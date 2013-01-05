def numToword(value):
    numdic={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",\
            10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",\
            17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",\
            60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand"}
    
    if value==1000:
        return numdic[1]+' '+numdic[1000]
    if value==0:
        return numidc[0]
    
    output=""
    if value / 100>0:
        output+=numdic[value / 100]+' '+numdic[100]

    if value % 100==0:
        return output
    elif value/100>0:
        output+=" and "

    value %= 100

    if value>=10 and value<20:
        output+=numdic[value]
    else:
        if value/10>0:
            output+=numdic[value/10*10]
            if value%10>0:
                output+='-'
        value%=10
        if value>0:
            output+=numdic[value]
    return output
count=0
for i in range(1,1001):
    count+=len(numToword(i).replace(' ','').replace('-',''))
    print numToword(i)
print count
