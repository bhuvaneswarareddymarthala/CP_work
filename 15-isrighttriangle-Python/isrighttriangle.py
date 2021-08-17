# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1 = (((x2-x1)**2)+((y2-y1)**2))
	s2 = (((x3-x2)**2)+((y3-y2)**2))
	s3 = (((x3-x1)**2)+((y3-y1)**2))
	if ((s1 == s2+s3) or (s2==s3+s1) or (s3==s1+s2)):
		return True
	return False

