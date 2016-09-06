def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2


def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

def make_center_percent(c, p):
    """ Construct an interval from center and tolerance.
    
    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    w = c * (p/100)
    return interval(c - w, c + w)

def percent(x):
   """Retunr the percentage tolerance of interval x.
   
   >>> percent(interval(1, 3))
   50.0
   """
   w  = ((upper_bound(x) - lower_bound(x))/2)
   c  = ((upper_bound(x) + lower_bound(x))/2)
   return (w/c)*100.0


def interval(a, b):
    """Construct an interval from a to b. """
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x. """
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x. """
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.
    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.
    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    result = zero
    for interval in seq:
        if 	non_zero(interval):
            result = add_interval(result, square_interval(interval))
    if non_zero(result):
        return result

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
	
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
	"""
    return reduce(add_interval, map(square_interval, filter(non_zero, seq)))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    return reduce(add_interval, (square_interval(interval) for interval in seq if non_zero(interval)))
	