# Dynamic Programming implementation of LCS problem
def compare(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2: return n1 - n2
    elif n1 == 0: return 0
    for i in xrange(n1):
        c = int(s1[i]) - int(s2[i])
        if c != 0: return c
    return 0
    
def max_string(s1, s2):
    return s1 if compare(s1, s2) >= 0 else s2
 
def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = ''
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + X[i-1]
            else:
                L[i][j] = max_string(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs
 
 
# Driver program to test the above function
X = "1352475813"
Y = "3185742531"
print "LCS is ", lcs(X, Y)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_0
