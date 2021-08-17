# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def pallin(n):
	n = str(n)
	rev = n[::-1]
	if str(n) == rev:
		return True
	return False

def nthlychrelnumbers(n):
	# your code goes here
	