# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	# p =[]
	# while(hand):
	# 	k = hand%10
	# 	hand = int(hand/10)
	# 	p.append(k)
	

	# return p[::-1]

	fd = hand //100
	sd = (hand%100)//10
	td = (hand%100)%10
	return fd,sd,td
