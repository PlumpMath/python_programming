def is_leaf(tree):
    return type(tree) != list

def flatten(tree):
    """Return a list containing the leaves of tree.
    
    >>> tree = [[1, [2], 3, []], [[4], [5, 6]], 7]
    >>> flatten(tree)
    [1, 2, 3, 4, 5, 6, 7]
    """
    if is_leaf(tree):
        print([tree])	
        return [tree]
    else:
        branch_list = [flatten(b) for b in tree]
        print(branch_list)
        return sum(branch_list, [])

lst = flatten([[1, [2], 3, []], [[4], [5, 6]], 7])
print(lst)

