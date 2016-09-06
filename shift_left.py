def shift_left(lst, n):
    """Shifts the lst over by n indices
    
	>>> lst = [1, 2, 3, 4, 5]
    >>> shift_left(lst, 2)
    >>> lst
    [3, 4, 5, 1, 2]
    """
    if n > 0:
        lst.insert(0, lst.pop())
        shift_left(lst, n - 1)

lst = [1, 2, 3, 4, 5]
shift_left(lst, 2)
print(lst)