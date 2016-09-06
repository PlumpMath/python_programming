def merge_iter(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge_iter([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_iter([], [2, 4, 6])
    [2, 4, 6]
    >>> merge_iter([1, 2, 3], [])
    [1, 2, 3]
    >>> merge_iter([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    new = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            new += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new += [lst2[0]]
            lst2 = lst2[1:]
    if lst1:
        return new + lst1
    else:
        return new + lst2

def merge_recur(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge_recur([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_recur([], [2, 4, 6])
    [2, 4, 6]
    >>> merge_recur([1, 2, 3], [])
    [1, 2, 3]
    >>> merge_recur([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] > lst2[0]:
        return [lst2[0]] + merge_recur(lst1, lst2[1:])
    else:
        return [lst1[0]] + merge_recur(lst1[1:], lst2)