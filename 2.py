#!/usr/bin/python
def fib():
    a,b = 1,2
    yield a
    yield b
    while True:
        a,b=b,a+b
        yield b
total=0
for i in fib():
    if i > 4000000:
        break
    if i % 2==0:
        total+=i
print total
