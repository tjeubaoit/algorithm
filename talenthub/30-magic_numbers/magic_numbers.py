
def find_amicable_pair_number(n):
	if n%2 == 0:
		s = 2 + n/2
		k = 1
	else:
		s = 0
		k = 2
	m = n/3	
	i = 3

	while i < m:
		if n%i == 0:
			m = n / i
			s += i + m
			# if s >= e: return -2
		i += k

	return s + 1

def find_magic_number(n):
	p = find_amicable_pair_number(n)

	if p == n: return 'PERFECT'
	elif find_amicable_pair_number(p) == n: return p
	else: return 'NONE'


# print find_amicable_pair_number(220)
# print find_amicable_pair_number(284)

# print find_magic_number(220)
# print find_magic_number(284)

print find_magic_number(int(raw_input().rstrip()))

