# Problem Set 1
# Name: Nathan Panchal
# Collaborators: n/a
# Time Spent: 
# 
balance = float(raw_input('Enter the outstanding balance on the credit card: '))
annual_rate = float(raw_input('Enter the annual interest rate: '))
min_payment_rate = float(raw_input('What is minimum monthly payment rate: '))

#test case 1
# balance = 4800
# annual_rate = .2
# min_payment_rate = .02

#test case 2
# balance = 4800
# annual_rate = .2
# min_payment_rate = .04

# #code from line 16 to line 27 is more accurate because the rounding is done at the end during the print statements. However this algorithm does not satisfy the answer key.
# month = 1
# for month in range(1, 12+1):
# 	min_payment = balance * min_payment_rate
# 	interest_paid = (annual_rate / 12) * balance
# 	principle_paid = min_payment - interest_paid
# 	balance = balance - principle_paid
# 	total_payment += min_payment
# 	print 'Month: ', month
# 	print 'Minimum Monthly Payment: %.2f' % min_payment
# 	print 'Principle Paid: %.2f' % principle_paid
# 	# print 'Principle Paid:', round(principle_paid, 2) #used to test different types of rounding in python
# 	# print 'Principle Paid:', principle_paid #kept unrounded answer to to comparte the various types of rounding
# 	print 'Remaining Balance: %.2f' % balance
# 	month =+ 1
# print 'RESTULT'
# print 'Total amount paid:', total_payment
# print 'Remaining balance:', balance

month = 1
total_payment = 0
for month in range(1, 12+1):
	min_payment = round(balance * min_payment_rate, 2)
	interest_paid = (annual_rate / 12) * balance
	principle_paid = round(min_payment - interest_paid, 2)
	balance = round(balance - principle_paid, 2)
	total_payment += min_payment
	print 'Month: ', month
	print 'Minimum Monthly Payment:', min_payment
	print 'Principle Paid:', principle_paid
	print 'Remaining Balance:', balance
	month =+ 1
print 'RESTULT'
print 'Total amount paid:', total_payment
print 'Remaining balance:', balance