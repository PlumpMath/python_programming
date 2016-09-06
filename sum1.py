def sum_naturals(n):
	"""Sum the first n natural numbers.
	
	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total

def sum_cubes(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + pow(k, 3), k + 1
	return total