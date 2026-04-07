def fib(n):
    a=0
    b=1
    
    if n == 0:
        return a
    elif n == 1:
        return b
    a,b = b, (a+b)
    return a, b

print(fib(4))