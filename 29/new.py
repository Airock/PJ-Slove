lst=[]
for i in range(2,101):
    for j in range(2,101):
      o=i**j
      if lst.count(o)==0:
          lst.append(o)
          
      
lst.sort()
print len(lst)
