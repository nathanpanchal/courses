#Problem Set: 1
#Name: Nathan Panchal
#Collaborators: n/a
#Time: 12/28/14 3:43PST
#

# Problem: Write a program that computes and prints the 1000th prime number.

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

counter = 0
n = 3
#print 2 ---if you wanted to print every prime in the range
while counter < 999:
    if is_prime(n):
        #print n ---for printing every step along the way
        counter = counter + 1
    n = n + 2
print n - 2 #comment this out and activate comment on line 23 and line 20 if you want to print every step along the way. 
