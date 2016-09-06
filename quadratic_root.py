from math import sqrt
def find_root(a, b, c):
    """Returns one of two roots of a quadratic equation
    
    Since there are two roots to quadratics, return the larger
    root. In other words, the + or - part of the quadratice equation
    should just be replaced with a +
    >>> find_root(1, 2, 1)
    -1.0
    >>> find_root(1, -7, 12)
    4.0
    """
    def discriminate(a, b, c):
        return sqrt((b*b)-4*a*c)
    return (-b + discriminate(a, b, c))/2 * a
