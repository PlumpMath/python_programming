from operator import floordiv, mod
def divide_exact(n, d):
	"""Return the quotient and remainder of dividing n by d.
	
	>>> quotient, remainder = divide_exact(2012, 10)
	>>> quotient
	201
	>>> remainder
	2
	"""
	return floordiv(n, d), mod(n, d)

def absolute_value(x):
	"""Return the absolute value of x
	>>> absolute_value(-3)
	3
	"""
	if x < 0:
		return -x
	elif x == 0:
		return 0
	else:
		return x
 
		