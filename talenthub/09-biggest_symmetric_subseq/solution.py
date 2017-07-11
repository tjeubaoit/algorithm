#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a string that consists of numeric characters from ′0′ to ′9′. A string c is called a substring 
# of the string a if it is possible to delete some characters from a to obtain c. For example, ‘ac’ 
# is a substring of ‘abc’ because we can obtain ‘ac’ by deleting character ‘b’ from ‘abc’. A string 
# x = c1c2 ... cL with length L is called symmetric if the string x and its reversed string cL cL−1 ... c1 
# are the same.

# Requirements: 
# • Write a program that find the symmetric substring that represents largest value. This string cannot 
# have 0 as its first character unless it has only 1 character.

# Input: 
# • The first line is the positive integer L which is the length of the string (1 ≤ L ≤ 2 000). 
# • The second line is the given string consists of L characters from ‘0’ to ‘9’.

# Output: 
# • Print the symmetric substring that represents largest value.

# FOR EXAMPLE: 
# Input: 
# 6 
# 128921

# Output: 
# 12921

def compare(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	if n1 != n2: return n1 - n2
	for i in xrange(n1/2 + 1):
		c = int(s1[i]) - int(s2[i])
		if c: return c
	return 0

def max(s1, s2):
	return s1 if compare(s1, s2) >= 0 else s2

def process_v2(s, accept_zero, fromIndex, toIndex, cache):
	if fromIndex == toIndex: return s[fromIndex]
	if fromIndex > toIndex: return ''

	result = cache[fromIndex][toIndex]
	if result: return result
	else: result = '0'

	last = fromIndex
	for i in range(fromIndex, toIndex + 1):
		if len(result) > toIndex - i + 1: break
		if not accept_zero and s[i] == '0': continue

		j = toIndex
		while j > last and j > i:
			if s[i] == s[j]:
				if j > last: last = j
				sub = process_v2(s, True, i + 1, j - 1, cache)
				tmp = s[i] + sub + s[i]
				if compare(result, tmp) < 0: 
					result = tmp
				break
			j = j - 1

		if len(result) == 1 and int(s[i]) > int(result): 
			result = s[i]

	cache[fromIndex][toIndex] = result
	return result

def process_v3(s, accept_zero, fromIndex, toIndex, cache, expected_size=1):
	if fromIndex == toIndex: return s[fromIndex]
	if fromIndex > toIndex: return ''

	ret = cache[fromIndex][toIndex]
	if ret: return ret
	else: ret = '0'    

	last = fromIndex
	len_ret = 1
	for i in range(fromIndex, toIndex + 1):
		max_size = toIndex - i + 1
		if expected_size > max_size or len_ret > max_size: break		
		if not accept_zero and s[i] == '0': continue

		j = toIndex
		while j > last and j > i:
			if s[i] == s[j]:
				if j > last: last = j
				sub = process_v3(s, True, i+1, j-1, cache, len_ret-2 if len_ret > 1 else 0)
				tmp = s[i] + sub + s[i]
				if compare(ret, tmp) < 0: 
					ret = tmp
					len_ret = len(tmp)
				break
			j = j - 1

		if len(ret) == 1 and int(s[i]) > int(ret): 
			ret = s[i]

	cache[fromIndex][toIndex] = ret
	return ret

def find_symmetric_substring(s):
	n = len(s)
	cache = [[None for x in range(n)] for y in range(n)]
	now = int(round(time.time() * 1000))
	# ret = process_v3(s, False, 0, len(s) - 1, cache)
	ret = process_v2(s, False, 0, len(s) - 1, cache)
	time_process = int(round(time.time() * 1000)) - now
	print time_process
	return ret


# l = raw_input()
# s = raw_input().rstrip()
# print find_symmetric_substring(s)


# s = raw_input()
# js_result = raw_input().rstrip()
# js_msg = raw_input()

import time
# now = int(round(time.time() * 1000))
# py_result = find_symmetric_substring(s)
# time_process = int(round(time.time() * 1000)) - now

# print js_result
# print py_result
# print js_msg
# print 'Py_took:', time_process


# print find_symmetric_substring('128921')
# print find_symmetric_substring('12312')
# print find_symmetric_substring('133122')
# print find_symmetric_substring('1352475813')
# print find_symmetric_substring('1352471358')
# print find_symmetric_substring('138247966')
# print find_symmetric_substring('17409')
# print find_symmetric_substring('13524713587788')
# print find_symmetric_substring('233288')
# print find_symmetric_substring('000008000')
# print find_symmetric_substring('0000')
# print find_symmetric_substring('002332880')
# print find_symmetric_substring('002339080632880')
# print find_symmetric_substring('48156358304135644341')
# print find_symmetric_substring('2400472561')
# print find_symmetric_substring('25495298763')
print find_symmetric_substring('0942223471610052173623274071394593650269236430060759666590130421519169425831308408936440226597616819481539584598479005412539179370765803167001419075596848380732487806606361522984611439595084706077458769083051656319315355786856345643254110554824092938640375734174025600649225913371138668106870582977077921017620006238390856876916750398311503837396054441085698504158550428422326267611172087304264969997002016001432809752967860460879941899170242003487911668258685522492279951504444765129842298225004014343619644251050098996489443116992326916023366936812309011008674639457449804399147852956399494999571809871670582303608989462539455374284228057619155892282354221653116622120204048007966079076852703955211103559343942375230731006903270326419610166450262533479169352314706777202939500886091944494100620805908233026086710254562145989005787113190484188798634428895410756344871296449396311017427724723862149720148433505747680446320983518683236097642193903070743442497027664646236454593465967884115744785448444')









