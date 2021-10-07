import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    first, second = 0,1
    if n == 1 or n == 2:
        return 1
    
    for i in range(n-1):
        first, second = second, first + second
    
    return second

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

