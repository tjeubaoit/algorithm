# Find the set of all integers a, b, c, d that satisfy the following conditions:
# 0 <= a^3 + b^3 + c^3 + d^3 <= N
# a^3 + b^3 = c^ + d3
# 0 <= a, b, c, d <= N

def find_satisfy_sets(N):
    a = 0
    d = dict()
    m = N // 2
    while pow(a, 3) <= m:
        for b in range(a):
            t = pow(a, 3) + pow(b, 3)
            if t > m:
                break
            if t in d:
                for cd in d[t]:
                    print(a, b, cd[0], cd[1])
                d[t].append((a, b))
            else:
                d[t] = [(a, b)]
        a += 1
        
    
if __name__ == '__main__':
    ret = find_satisfy_sets(10000)    
