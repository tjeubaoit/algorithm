#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_symmetrical_substring(s):
	mid_max = '-1'
	positions = []
	result = ''
	size = len(s)
	last = size

	for i in range(0, size):
		j = len(s) - 1
		ok = False
		while j > i:
			if s[i] == s[j]:
				if positions and j > last:
					if s[j] > s[last]: positions.pop()
					else: continue

				positions.append(j)
				mid_max = '-1'
				last = positions[-1]
				ok = True
				break			
			j -= 1
		if not ok:
			if int(s[i]) > int(mid_max) and i < last:
				mid_max = s[i]		
	
	if positions:
		first = positions[0]	
		if s[first] == '0':
			if (len(positions) == 1 and mid_max == '-1'): return '0'
			else: del positions[0]	

	for pos in positions:
		result += s[pos]

	if int(mid_max) >= 0:
		result += mid_max

	for pos in reversed(positions):
		result += s[pos]

	return result


# raw_input()
# s = raw_input().rstrip()
# print find_symmetrical_substring(s)


# print find_symmetrical_substring('128921')
# print find_symmetrical_substring('12312')
# print find_symmetrical_substring('13312')
# print find_symmetrical_substring('1352475813')
# print find_symmetrical_substring('1352471358')
# print find_symmetrical_substring('138247966')
print find_symmetrical_substring('13524713587788')
