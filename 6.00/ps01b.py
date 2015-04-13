# Problem Set 1
# Name: Nathan Panchal
# Collaborators: n/a
# Time: 12/28/14 5:16PST
#
from math import *

def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num % 2 == 0 and num != 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

n = int(raw_input("Please provide an n value: "))
total = 0
for num in range(2, n + 1): #"+1" is used because the range function is exclusive
	if is_prime(num):
		total = total + log(num)

print total
print n
print (n / total)