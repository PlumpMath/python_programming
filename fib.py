def fib(k):
    """Compute the kth Fibonacci number.
    >>> fib(1)
    0
    >>> fib(2)
    1
    >>> fib(11)
    55
    """
    prev, curr = 1, 0 	# curr is the first fibonacci number
    for _ in range(1, k):
        prev, curr = curr, prev+curr
    return curr
    
	"""
    prev, curr = 0, 1  # prev is the first Fibonacci number.
    for _ in range(1, k):
         prev, curr = curr, prev + curr
    return prev
    
    k = 1;  prev = 0, curr = 1; return prev
    k = 2;  prev = 1, curr = 1; return prev
    k = 3;  prev = 1, curr = 2; return prev
    k = 4;  prev = 2, curr = 3; return prev
    k = 5;  prev = 3, curr = 5; return prev 
    
	====================================                               0, 1, 1, 2, 3,  5,  8
                                                                       0, 2, 2, 4, 6, 10, 16   
    prev, curr = 1, 0  # curr is the first Fibonacci number.
    for _ in range(1, k):
         prev, curr = curr, prev + curr
    return curr
	
	k = 1;  prev = 1, curr = 0; return curr
	k = 2;  prev = 0, curr = 1; return curr
	k = 3;  prev = 1, curr = 1; return curr
	k = 4;  prev = 1, curr = 2; return curr
	k = 5;  prev = 2, curr = 3; return curr
	
	=======================================
	
    prev, curr = 2, 0  # curr is the first Fibonacci number.
    for _ in range(1, k):
         prev, curr = curr, prev + curr
    return curr
	
	k = 1;  prev = 2,  curr = 0;  return curr
	k = 2;  prev = 0,  curr = 2;  return curr
    k = 3;  prev = 2,  curr = 2;  return curr
    k = 4;  prev = 2,  curr = 4;  return curr
	"""