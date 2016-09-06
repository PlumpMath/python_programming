def product(n, term):
    """Return the product of the first n terms in a sequence
	
	term --- a function that takes one argument
	
	>>>product(4,square)
	576
	"""
    if n == 1:
        return 1
    else:
        return n * product(n-1, term)

def identity(k):
    return k

def square(x):
    """ Retrun x squared"""
    return x * x

		
def factorial(n):
	""" Return n factorial by calling product
		
	>>> factorial(4)
	24
	"""
	assert n >= 0	
	return product(n, identity)
    
result = factorial(4)
print(result)