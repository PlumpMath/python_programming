fibcache = {}
def sum_fibonacci(n):
    """Compute the nth Fibonacci number.

    >>> sum_fibonacci(35)
    9227465
    >>> sum_fibonacci(10)
    55
    >>> sum_fibonacci(0)
    0
    >>> sum_fibonacci(1)
    1
    >>> sum_fibonacci(5)
    5
    """
    if n == 0:
        fibcache[0] = 0
        return fibcache[0]
    elif n == 1:
        fibcache[1] = 1
        return fibcache[1]
    else:
        sum_left= 0
        sum_right = 0
        if n-2 in fibcache.keys():
            sum_left  += fibcache[n-2]
        else:
            sum_left += sum_fibonacci(n-2)
            fibcache[n-2] = sum_left
        if n-1 in fibcache.keys():
            sum_right += fibcache[n-1]
        else:
            sum_right += sum_fibonacci(n-1)
            fibcache[n-1] = sum_right
        return sum_left + sum_right