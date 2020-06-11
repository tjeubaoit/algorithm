#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the palindromeIndex function below.
def palindromeIndex(s):
    l, r = 0, len(s) - 1
    return palindromeIndexRecursive(s, l, r, -1)


def palindromeIndexRecursive(s, l, r, ans):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        elif ans > 0:
            ans = -1
            break

        ret1 = ret2 = -1
        if s[l+1] == s[r]:
            ret1 = palindromeIndexRecursive(s, l+2, r-1, l)
        if s[l] == s[r-1]:
            ret2 = palindromeIndexRecursive(s, l+1, r-2, r)
        if ret1 == -1 and ret2 == -1:
            return -1
        else:
            return max(ret1, ret2)
    return ans


if __name__ == '__main__':
    s = 'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
    ret = palindromeIndex(s)
    print(ret)
