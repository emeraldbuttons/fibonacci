import sys

def fib(x):
    f = [0,1]
    while(x > len(f)):
        new_int = f[len(f) - 1] + f[len(f) - 2]
        f.append( new_int )
    return f

def factorial(x):
    z = 1
    for y in range(1,x+1):
        z *= y
    return z
