# Problem Set 1
# Name: Nathan Panchal
# Collaborators: n/a
# Time Spent:
#
principle = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

#test case 1
# principle = 1200
# annual_rate = .18

#test case 2
# principle = 32000
# annual_rate = .2

monthly_payment = 0
monthly_rate = annual_rate / 12
balance = principle #must define variable 'balance' here because it is used in the first while test

while balance > 0: #tests if the current fixed monthly payment amount. If the balance from the nested while is less <= zero then we know the current monthly amount works
	monthly_payment += 10 #the previously tested value for monthly_payment did not work so we increment by the chosen amount.
	balance = principle #resets the balance back to the principle amount because in the nested while we affect the value of balance.
	months = 0 #months are reset to 0 in preparation for a new simulated year in the nested while.
	while months < 12 and balance > 0: #simulating a 12 month period with the current fixed monthly payment amount.
		months += 1
		interest = monthly_rate * balance
		balance -= monthly_payment
		balance += interest
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', monthly_payment
print 'Number of months needed:', months
print 'Balance:', round(balance, 2)