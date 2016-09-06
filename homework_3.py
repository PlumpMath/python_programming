def interval(a, b):
    """Construct an interval from a to b. """
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x. """
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x. """
    return x[1]

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.
    
    Division is implemented as the multiplication of x by the reciprocal of y.
    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert (lower_bound(y) > 0  or upper_bound(y) < 0), "what it means to divide by an interval that spans zero"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.
    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    return interval(lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y))

def str_interval(x):
    """Return a string representation of interval x.
    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.
    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

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

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
	value in y, using as few multiplications as possible.
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(interval(-2, -1), interval(4, 8)))
    '-16 to -4'
    >>> str_interval(mul_interval_fast(interval(-1, 3), interval(-4, 8)))
    '-12 to 24'
    >>> str_interval(mul_interval_fast(interval(-1, 2), interval(-8, 4)))
    '-16 to 8'
    """
    if lower_bound(x) >= 0:
        if lower_bound(y) >= 0:
            return interval(0, upper_bound(x)*upper_bound(y))
        else:  # lower_bound(y) < 0
            if upper_bound(y) >= 0:
                return interval(upper_bound(x)*lower_bound(y), upper_bound(x)*upper_bound(y))
            else: 
                return interval(upper_bound(x)*lower_bound(y), lower_bound(x)*upper_bound(y))			
    else: #lower_bound(x) < 0
        if upper_bound(x) >= 0:
            if lower_bound(y) >= 0:
                return interval(lower_bound(x)*upper_bound(y), upper_bound(x)*upper_bound(y))
            else: #lower_bound(y) < 0
                if upper_bound(y) >= 0:
                    if abs(lower_bound(x)) > abs(upper_bound(x)):
                        return interval(lower_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y))
                    elif abs(lower_bound(x)) < abs(upper_bound(x)):
                        return interval(upper_bound(x)*lower_bound(y), upper_bound(x)*upper_bound(y))
                    else: # abs(lower_bound(x)) < abs(upper_bound(x))
                        return interval(lower_bound(x)*upper_bound(y), upper_bound(x)*upper_bound(y))
                else: #upper_bound(y) < 0
                        return interval(upper_bound(x)*lower_bound(y), lower_bound(x)*lower_bound(y))        
        else:  #upper_bound(x) < 0
            if lower_bound(y) >= 0:
                return interval(lower_bound(x)*upper_bound(y), upper_bound(x)*lower_bound(y))
            else:   # lower_bound(y) < 0
                if upper_bound(y) >=0:
                    return interval(lower_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y))
                else:
                    return interval(upper_bound(x)*upper_bound(y), lower_bound(x)*lower_bound(y))

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

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))
