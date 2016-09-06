def is_leaf(tree):
    return type(tree) != list


def right_binarize1(tree):
    """Return a right-branching binary tree with the structure of the input.

    >>> right_binarize1([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    >>> pangram = [['the', 'quick', 'brown', 'fox'], ['jumped', 'over', 'a', 'lazy', 'dog']]
    >>> right_binarize1(pangram)
    [['the', ['quick', ['brown', 'fox']]], ['jumped', ['over', ['a', ['lazy', 'dog']]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize1(b) for b in tree]

def right_binarize2(tree):
    """Return a right-branching binary tree with the structure of the input.

    >>> right_binarize2([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    >>> pangram = [['the', 'quick', 'brown', 'fox'], ['jumped', 'over', 'a', 'lazy', 'dog']] 
    >>> right_binarize2(pangram)
    [['the', ['quick', ['brown', 'fox']]], ['jumped', ['over', ['a', ['lazy', 'dog']]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]        
    return [right_binarize2(tree[0]), right_binarize2(tree[1]) ]