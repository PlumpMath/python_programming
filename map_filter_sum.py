def fib(k):
    """Compute kth fibonacci number.
	
	>>> fib(1)
	0
	>>> fib(2)
	1
	>>> fib(11)
	55
	"""
    def recursive_fib(prev, curr, k):
        if k - 1 == 0:
             return curr
        else:
             return recursive_fib(curr, prev + curr, k - 1)
    return recursive_fib(1, 0, k)

def iseven(n):
    if n % 2 == 0:
       return True

def sum_even_fibs(n):
    """Sum the first even fibonacci numbers
    
	>>> sum_even_fibs(11)
	44
	"""
    return  sum(filter(iseven, map(fib, range(1, n + 1))))

def sum_even_fibs_gen(n):
    """Sum the first even fibonacci numbers
    
	>>> sum_even_fibs_gen(11)
	44
	"""
    return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)