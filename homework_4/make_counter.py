def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a', 3)
    3
    >>> c('a', 5)
    8
    >>> c('b', 7)
    7
    >>> c('a', 9)
    17
    >>> c2 = make_counter()
    >>> c2(1, 2)
    2
    >>> c2(3, 4)
    4
    >>> c2(3, c('b', 6))
    17
    """
    d = {}	
    def counter(key, value):
        d[key] = d.get(key, 0) + value
       	return d[key]
    return counter
    """-m doctest gives some weird failure despite all above test case pass"""