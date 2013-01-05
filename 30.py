print reduce(lambda x,y:x+y,filter(lambda i:i==reduce(lambda x,y:x+y,[int(j)**5 for j in str(i)]),range(2,360000)))
