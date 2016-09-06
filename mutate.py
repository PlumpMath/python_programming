def map_mut(fn, lst):
    """Maps fn onto lst by mutation.

    >>> lst = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, lst)
    >>> lst
    [1, 4, 9, 16]
    """
    def mutate(index):
        if index < len(lst):
            lst[index] = fn(lst[index])
            mutate(index + 1)
    mutate(0)
lst = [1, 2, 3, 4]
map_mut(lambda x: x**2, lst)
print(lst)