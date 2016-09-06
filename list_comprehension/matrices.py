def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    return [ [x[i][j] + y[i][j] for j in range(len(y))] for i in range(len(x))]
    