def fib(x):
    if x < 2:
        return x
    return fib(x-2) + fib(x-1)

def fib1(x):
     a,b = 1,1
     for i in range(x-1):
      a,b = b,a+b
     return a

