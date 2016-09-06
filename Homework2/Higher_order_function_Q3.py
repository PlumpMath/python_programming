from operator import mul, add

def double(f):
    """Return a function that applies f twice.
    f -- a funtion that takes one argument
    
    >>> double(square)(2)
    16
    """
    def g(x):
        return f(f(x))	
    return g

def successor(x):
    return x + 1


def square(x):
    return mul(x, x)

print(double(square)(2))
