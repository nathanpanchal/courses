# Problem Set 2
# Name: Nathan Panchal
# Collaborators: n/a
# Time: 12/31/14 5:16PST
#
x = int(raw_input("Please privide a value for your fist nugget pack x: "))
y = int(raw_input("Please privide a value for your fist nugget pack y: "))
z = int(raw_input("Please privide a value for your fist nugget pack z: "))

def solution_test(n):
	for a in range(0, (n/x)+1):
		for b in range(0, (n/y)+1):
			for c in range(0, (n/z)+1):
				if a*x + b*y + c*z == n:
					return True

n = 200 #in this case we are counting down from a fixed n value so there is not need to ask for raw_input to define this variable
while solution_test(n) == True and n > 0: #n should logically never be less than 0 otherwise you would be giving McDonalds nuggest instead of buying them
	n = n - 1
print "Given package sizes {x}, {y}, and {z}, the largest number of McNuggets that cannot be bought in exact quantity is: {n}".format(x=x,y=y,z=z,n=n) #my favorite mentod for string intorplation in python