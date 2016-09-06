def hailstone(n, count = 1):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print(n)
        return count
    if n % 2 == 0:
        print(n)
        return hailstone(n // 2, count + 1)
    else:
        print(n)
        return hailstone(3 * n + 1, count + 1)