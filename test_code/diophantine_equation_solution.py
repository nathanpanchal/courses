# This code was originally used to calculate what combination of chicken nugget packs
# are needed to have a desired n amount.

n = int(raw_input("Please provide an n value: "))

# Define the coefficients x,y,z or the size of the chicken nugget packs.
x = 6
y = 9
z = 20

# We only need to find a value up to n/x
# "+1" is used because the range in the for function is exclusive. 
for a in range(0, (n/x)+1):
	for b in range(0, (n/y)+1):
		for c in range(0, (n/z)+1):
			if a*x + b*y + c*z == n:
				# if the desired n has multiple solutions all of them will be printed
				print (a, b, c)
