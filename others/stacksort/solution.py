stack_0 = [3, -3, 1, 5, 9, 2, 11, 4, 7, 15, 8]
stack_1 = []
size = len(stack_0)

for i in range(0, len(stack_0) / 2):
	nmin = stack_0.pop()
	while len(stack_0) > i:
		top = stack_0.pop()
		if (top < nmin):			
			stack_1.append(nmin)
			nmin = top
		else:
			stack_1.append(top)
	stack_0.append(nmin)

	nmax = stack_1.pop()
	while len(stack_1) > i:
		top = stack_1.pop()
		if (top > nmax):
			stack_0.append(nmax)
			nmax = top		
		else:
			stack_0.append(top)
	stack_1.append(nmax)

while len(stack_1) > 0:
	stack_0.append(stack_1.pop())

print ', '.join(str(x) for x in stack_0)