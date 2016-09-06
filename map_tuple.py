def map_tuple(func, tup):
    """Applies func to each element of tup and returns a new tuple.
	
	>>> a = (1, 2, 3, 4)
	>>> func = lambda x: x * x
	>>> map_tuple(func, a)
	(1, 4, 9, 16)
	"""
    new_tuple = ()
    for itup in tup:
        new_tuple += (func(tup[count]),)
    return new_tuple

def map_tuple_recursive(func, tup):
    """Applies func to each element of tup and returns a new tuple.

    >>> a = (1, 2, 3, 4)
	>>> func = lambda x: x * x
	>>> map_tuple(func, a)
	(1, 4, 9, 16)
	"""
    if not tup:
            return ()
        else:
            return  map_tuple_recursive(func, tup[:-1])   + (func(tup[-1]), )

def min_element(tup):
    def find_min(tup, min):
        if not tup:
           return min
        else:
           min = tup[0] if tup[0] < min else min
           return min_element(tup[1:], min)
    if tup:
        return find_min(tup[1:], tup[0])