
import math

def fibonacci_recursive(n):
    # Write your code here.
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2) if n > 1 else n    

def fibonacci_not_recursive(n):
    if n < 2: return n    

    fb = [0, 1]
    for i in xrange(2, n + 1):
        fb[i % 2] = fb[0] + fb[1]

    return fb[n % 2]

def fibonacci_best(n):
    """And Binet's formula / Golden Rat"""
    return round(pow((1 + math.sqrt(5)) / 2, 3) / math.sqrt(5))

def fibonacci_hackerrank(n):
    fib = lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)
    return fib(int(input()))
    
n = int(raw_input())
print(fibonacci_recursive(n))