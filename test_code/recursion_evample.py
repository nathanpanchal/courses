def simple_exponent(b, n):
	# This is the base case.
	if n == 0
		return 1
	else:
		# This is the recursive definitoin. It will keep unwinding the recursive calls until
		# it hits the base case.
		return b * simple_exponent(b, n-1)