def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if x == 1 and y == 1:
        return 1
    count = 0
    if x > 0:
        count += paths(x-1, y)
    if y > 0:
        count += paths(x, y-1)
    return count	
