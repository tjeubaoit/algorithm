
def pyraminers(m, n, p):
	t = (n / p)
	if t == 0: return -1
	else: return m / t

# m = 1000
# n = 60
# p = 15

s = raw_input().rstrip().split(' ')
m = int(s[0])
n = int(s[1])
p = int(s[2])

print pyraminers(m, n, p)
