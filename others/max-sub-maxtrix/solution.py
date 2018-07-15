
MIN_VALUE = -2147483648


def find_max_sub_seq(a, size):
    max_so_far = MIN_VALUE
    max_ending_here = 0
    s = 0
    sub = (0, -1)
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            sub = (s, i)
            
    if sub[1] == -1:
        for i in range(0, size):
            if a[i] > max_so_far:
                max_so_far = a[i]
                sub = (i, i)
            
    return max_so_far, sub
 

########################
# O(n^3) complexity
########################    
def find_max_sub_matrix_better(a, m, n):
    msf = MIN_VALUE
    sub = ((0, 0), (0, 0))
      
    for top in range(0, m):
        meh = 0
        t = [0]*n
        for i in range(top, m):
            for j in range(0, n):
                t[j] += a[i][j]
            meh, (s, e) = find_max_sub_seq(t, n)
            if meh > msf:
                msf = meh
                sub = ((top, s), (i, e))
                
    return msf, sub
    

########################
# O(n^3) complexity
########################
def find_max_sub_matrix(a, m, n):
    msf = MIN_VALUE
    sub = ((0, 0), (0, 0))
      
    for top in range(0, m):
        c = [[0]*n for _ in range(top, m)]
        meh = 0
        for row in range(top, m):
            i = row - top
            sj = t = 0
            for j in range(0, n):
                t += a[row][j]
                c[i][j] = t if i == 0 else c[i-1][j] + t
                meh = c[i][j] if sj == 0 else c[i][j] - c[i][sj-1]
                
                if meh < 0:
                    meh = 0
                    sj = j+1
                elif (msf < meh):
                    msf = meh
                    sub = ((top, sj), (row, j))

    return msf, sub
    

# a = [3, -2, -3, 4, -1, -2, 1, 5, -3]
a = [-3, -2, -3, -4, -1, -2, -1, -5, -3]
m, (s, e) = find_max_sub_seq(a, len(a))
print(m, s, e, a[s:e+1])


aa = [
    [5, 4, -10, -6, 4],
    [1, -2, 7, 16, -11],
    [-7, 19, -2, 10, 6],
    [-2, -7, 4, 2, 4],
    [-1, -6, 8, -3, -2]
]

n = len(aa)
import time

now = time.time()
m, (s, e) = find_max_sub_matrix(aa, n, n)
print(m, s, e, (time.time() - now)*1000)

now = time.time()
m, (s, e) = find_max_sub_matrix_better(aa, n, n)
print(m, s, e, (time.time() - now)*1000)

