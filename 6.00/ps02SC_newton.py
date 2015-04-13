# Problem Set 2
# Name: Nathan Panchal
# Collaborators: none
# Time: 

# The test polynomial
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)

# evaluates a polynomial for a given x
def evaluate_poly(poly, x):
	ans = 0.0
	for n in range(len(poly)):
		ans += poly[n] * (x ** n)
	return ans


# returns a list containing the coeffiencts for the derivitive of poly
def compute_deriv(poly):
	# initializes an empty list
	derivitive = []
	# if the polynomial is one term in length the derivitive is 0.0 
	if len(poly) < 2:
		return (0.0,)
	for n in range(len(poly)):
		derivitive.append(poly[n] * n)
	# the instructions say to return a tuple. This line converts the list to a tuple
	return tuple(derivitive)


# computes the root of a polynomial
def compute_root(poly, x_0, epsilon):
	root = x_0
	iterations = 1
	while abs(evaluate_poly(poly, root)) >= epsilon:
		# This is newton's method for iterating through a guess to find a rood that is less
		# than epislon away from the true root.
		root = root - evaluate_poly(poly, root) / evaluate_poly(compute_deriv(poly), root)
		iterations += 1
	return [root, iterations]

print compute_root(poly, 0.1, 0.0001)