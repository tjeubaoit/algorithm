#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_match_v4(s1, s2, size):
    return bm(s2 + s2[:-1], s1)

def find_uniques(lines, n, l):
    ignores = []
    count = 0
    for i in xrange(n):
        if i in ignores: continue
        if i < n-1:
            p = lines[i]
            os = occ_shift(p)
            ms = matching_shift(p)
            for j in range(i+1, n):
                if j in ignores: continue
                s = lines[j] + lines[j][:-1]
                if bm_preprocess(s, p, os, ms, 2*(l-1) + 1, l) is not None:
                    ignores.append(j)
        count += 1
    return count

def bm_preprocess(s, p, os, ms, n, m): # the Boyer-Moore algorithm
    j = 0
    while (j <= n-m):
        i = m-1
        while (i >= 0) and (p[i] == s[j+i]): i = i-1
        if (i == -1):
            # print "Match at position ", j
            i = 0
            return j            
        j = j + max(ms[i], i-os[s[i+j]])

def occ_shift(p): # compute the occurrance shift array
    m  = len(p)
    atoz  = map(chr, range(97, 123)) # list from 'a' to 'z'
    os = dict.fromkeys(atoz, -1)     # 26 characters, all os['c'] = -1 at first
    for i in xrange(m):
        os[p[i]] = i
    return os

def suffix(p): # compute the lcs array
    m = len(p); 
    lcs = [0]*m
    lcs[m-1] = m
    l = r = m-1
 
    for i in range(m-2, -1, -1): # i from m-2 downto 0
        if ((l < i) and (lcs[i+m-1-r] < i-l)):
            lcs[i] = lcs[i+m-1-r]
        else:
            l = min(l, i)
            r = i
            while ((l >=0) and (p[l] == p[l+m-1-i])): l = l-1
            lcs[i] = r-l
 
    return lcs

def matching_shift(p): # compute the matching shift array
    m = len(p)
    i = 0
    ms = [0]*m
    lcs = suffix(p)
    for k in range(1, m+1):
        if (k == m) or (lcs[m-1-k] == m-k):
            while (i < k):
                ms[i] = k
                i = i+1
    for k in range(m-1, 0, -1):
        ms[m-1-lcs[m-1-k]] = k
    return ms


# params = raw_input().rstrip().split(' ')
# n = int(params[0])
# l = int(params[1])

# lines = []
# for i in xrange(n):
#   s = raw_input().rstrip()
#   lines.append(s)

# print find_uniques(lines, n, l)


num_unique = 102
l = 15
n = 102

def make_random_input():
    import random
    import string

    lines = []
    for i in xrange(num_unique):
        line = "".join([random.choice(string.letters[:26]) for i in xrange(l)])
        lines.append(line)

    with open('data.in', 'w') as f:
        for i in xrange(n):
            pos = random.randint(0, len(line) - 1)
            line = lines[i % num_unique]
            f.write(line[pos:] + line[:pos] + '\n')

# make_random_input()

lines = []
with open('data.in', 'r') as f:
    for line in f:
        lines.append(line.rstrip())

import time
now = int(round(time.time() * 1000))
print 'Unique', find_uniques(lines, len(lines), l)
print 'Time took:', (int(round(time.time() * 1000)) - now)


def run_test(s1, s2):
    return check_match_v4(s1, s2, 0) is not None

# import random
# import string

# ok = True
# # ok = False
# while ok:
# 	line = "".join([random.choice(string.letters[:10]) for i in xrange(200)])
# 	for pos in xrange(len(line)):
# 		if not run_test(line, line[pos:] + line[:pos]):
# 			print 'Error line: ', line, line[pos:] + line[:pos]
# 			ok = False
# 			break
#         else: print 'ok'

# print suffix("ccgijcbibihbdcc")
# print bm("ccgijcbibihbdccccgijcbibihbdc", "cgijcbibihbdccc")
# print check_match_v4("hbgejadjjfihfai", "ihbgejadjjfihfa", 0)
# print check_match_v4("etqkrqchcytdbny", "ytdbnyetqkrqchc", 0)
# print check_match_v4("auvhiwlocxlvnky", "lvnkyauvhiwlocx", 0)

