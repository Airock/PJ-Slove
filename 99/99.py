import math
f=open("base_exp.txt")
input=f.read().split("\n")

maxline=0
max=0.0
for i in range(len(input)):
    a=input[i].split(",")
    curr=float(a[1])*math.log10(float(a[0]))
    if curr>max:
        max=curr 
        maxline=i+1
print max
print maxline


