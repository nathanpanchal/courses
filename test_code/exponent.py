# This is a simple pice of code that illustrates the usefulness of a recursion

def exponent(base, power):
    if power == 0:
        return 1
    else:
    	# The recursion occurs here. Notice we are reducing the power of the exponent
    	# each time the variables run through the recursive function eventually we hit the
    	# base case and return 1.
        return base * exponent(base, power - 1)