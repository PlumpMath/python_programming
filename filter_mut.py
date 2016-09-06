def filter_mut(pred, lst):
    """Filters lst by mutating it.
    
    >>> lst = [1, 2, 3, 4, 5]
    >>> is_even = lambda x: x % 2 == 0
    >>> filter_mut(is_even, lst)
    >>> lst
    [2, 4]
    """
    def filter(index):
        if index < len(lst):
            if pred(lst[index]):
                filter(index + 1)
            else:
                lst.pop(index)
                filter(index)
    filter(0)

lst = [1, 2, 3, 4]
is_even = lambda x: x % 2 == 0
filter_mut(is_even, lst)
print(lst)