# A tree is a either a single value called a leaf or a sequence of trees

def is_leaf(tree):
    return type(tree) != list

def count_leaf(tree):
    if is_leaf(tree):
        return 1
    branch_counts = []
    for b in tree:
        branch_counts.append(count_leaf(b))
    return sum(branch_counts)

def count_leaf_comprh(tree):
    if type(tree) != list:
        return 1
    branch_counts = [count_leaf_comprh(b)) for b in tree]
    return sum(branch_counts)

count_leaf([[1, [2], 3, []], [[4], [5,6]], 7])