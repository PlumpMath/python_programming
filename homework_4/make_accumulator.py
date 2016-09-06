def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.
    
    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    def accumulate(n):
        accumulate.lst.append(n)
        total = 0
        for item in accumulate.lst:
            total += item
        return total
    accumulate.lst = []
    return accumulate
    """How can I think of writing pure functional code for above program(i.e., 
    without any state change)? Can I?
    """