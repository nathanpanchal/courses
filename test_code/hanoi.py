def hanoi(n, f, t, s):
	if n == 1:
		print "Move " + f + " to " + t
	else:
		hanoi(n-1, f, s, t)
		hanoi(1, f, t, s)
		hanoi(n-1, s, t, f)

size = int(raw_input("What is the size of the original stack?"))

hanoi(size, 'original', 'target', 'spare')