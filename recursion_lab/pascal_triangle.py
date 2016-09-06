def pascal_with_memoization(row, column):
    """
    >>> pascal_with_memoization(3, 2)
    3
    >>> pascal_with_memoization(3, 3)
    1
    >>> pascal_with_memoization(5,4)
    5
    """
    cache = {}
    for row_indx in range(0, row + 1):
        cache.setdefault(row_indx, []).insert(0, 1)
    for col_indx in range(1, column + 1):
        cache.setdefault(0, []).insert(col_indx, 0)	
    def pascal(row, column):
        if column == 0:
            return cache[row][column]
        elif row  == 0:
            return  cache[row][column]
        else:
            value_1 = 0
            value_2 = 0
            lst = cache[row-1]
            if len(lst) > column: 
                value_1 = cache[row-1][column]
                value_2 = cache[row-1][column-1]
            elif len(lst) > column - 1:
                value_1 = pascal(row-1, column)
                value_2 = cache[row-1][column-1]  
                cache.setdefault(row-1, []).insert(column, value_1)
            else:
                value_1 = pascal(row-1, column)
                value_2 = pascal(row-1, column-1)
            return value_1 + value_2
    return pascal(row, column)