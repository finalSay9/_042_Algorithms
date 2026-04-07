#creating a sequence for finding the fibonacci sequence

def fib(number):
    a = 0
    b = 1
    if number == 1:
        return number
    else: 
        fib(number -1) + fib(number + 1)

print(fib(4))
