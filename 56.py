print max(map(lambda input:reduce(lambda x,y:x+y, [int(x) for x in str(input)]),\
        [x**y for x in range(90,100) for y in range(90,100)]))
