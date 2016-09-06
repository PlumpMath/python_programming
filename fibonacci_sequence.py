empty_rlist = None
#Representation - start
#Constructor
def rlist(first, rest):
    return(first, rest)

#Selector
def first(s):
    return s[0]

def rest(s):
    return s[1]

#Representation - end

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

def fib_sequence(k):
    prev, curr = 1, 0
    def generate_sequence(prev, curr, k):
        if k == 0:
           return empty_rlist
        elif k == 1:
           return rlist(curr, empty_rlist)
        else:
           return rlist(curr, generate_sequence(curr, prev+curr, k - 1))
    return generate_sequence(prev, curr, k)

def range_seq_generator(start, end):
    starting_element = start
    def number_sequence(k):
        if k + 1 == end:
            return rlist(k, empty_rlist)
        else:
            return rlist(k, number_sequence(k+1))
    return number_sequence(starting_element)