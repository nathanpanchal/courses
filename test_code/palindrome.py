# written by MIT professor. It is a more complex example of recursion. Some of the variable
# names are changed.

def toChars(s):
	import string
	s = string.lower(s)
	ans = ''
	# breaks the string into its characters
	for c in s:	
		if c in string.lowercase:
			ans = ans + c
	# returns the complied list of characters
	return ans


def isPal(s):
	if len(s) <= 1:
		return True
	else:
		# Check if the fist and last character of the string are equal and continue to check
		# remaining characters in the same fashion until you reach a string of length 1 or 0
		return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
	# Returns True if s is a palindrome and False otherwise
	print isPal(toChars(s))

s = raw_input('Enter a string: ')

isPalindrome(s)