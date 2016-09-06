from operator import add
from operator import mul

def square(x):
    """ Retrun x squared"""
    return x * x


def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    if n == 0:
        return start
    else:
        next_acc = combiner(term(n), start)
        return accumulate(combiner, next_acc, n-1, term)

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    assert n >= 0
    return accumulate(add, 0, n, term)
    
	

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    assert n > 0
    return  accumulate(mul, 1, n, term)    

result =  summation_using_accumulate(4, square)
print(result)
result = product_using_accumulate(3, square)
print(result)
	