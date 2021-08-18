# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isprime(n):
	if n>1:
		for i in range(2,int(n/2)+1):
			if(n%i)==0:
				return False
			else:
				return True
	else:
		return False

def is_happy(n):
	

def fun_nth_happy_prime(n):

	return 0