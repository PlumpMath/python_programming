def square(x):
    return x * x

def compose1(f, g):
    """Return a function of x that computes f(g(x))"""
    return lambda x: f(g(x))

from functools import reduce

def repeated(f, n):
    """Return the function that computes the nth application of f, for n>= 1.
    
    f -- a function that takes one argument
    n -- a positive integer
    
    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    assert type(n) == int and n > 0, "Bad n"
    return reduce(compose1, [f for i in range(n)])