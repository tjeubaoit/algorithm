def is_prime(n):
    if n == 2: 
        return True
    elif n == 1 or n & 1 == 0: 
        return False
    
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    print 'Prime' if is_prime(n) else 'Not prime'