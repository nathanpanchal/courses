# Problem Set 2
# Name: Nathan Panchal
# Collaborators: n/a
# Time: 12/30/14 9:21PST
#
def solution_test(n):
	for a in range(0, (n/6)+1):
		for b in range(0, (n/9)+1):
			for c in range(0, (n/20)+1):
				if a*6 + b*9 + c*20 == n:
					return True

n = 50
while solution_test(n) == True:
	n = n - 1
print "Largest number of McNuggets that cannot be bought in exact quantity: {}".format(n) #I like the interpolation in Ruby more
