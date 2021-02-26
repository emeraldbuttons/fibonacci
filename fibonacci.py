import sys

def fib(x):
    f = [0,1]
    while(x > len(f)):
        new_int = f[len(f) - 1] + f[len(f) - 2]
        f.append( new_int )
    return f