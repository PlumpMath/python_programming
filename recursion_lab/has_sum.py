def f(sum, n1, n2):
    """
    >>> f(1, 3, 5)
    False
    >>> f(5, 3, 5) # 1(5) + 0(3) = 5
    True
    >>> f(11, 3, 5) # 2(3) + 1(5) = 11
    True
    >>> f(189, 4, 9)
    True
    """
    def has_sum(sum, n1, n2, x=0, y=0):
        if (n1 + n2)  == sum:
            return True
        if (has_sum.memoiz) and ((n1 + n2)  > sum): # inefficient base case, need to improve using math
            return False
        result1 = False
        result2 = False
        if (x+1, y) not in has_sum.memoiz:
            has_sum.memoiz.add((x+1, y)) #memoiz
            result1 = has_sum(sum, (x+1)*orig_n1, y*orig_n2, x+1, y)
        if (x, y+1) not in has_sum.memoiz:
            has_sum.memoiz.add((x, y+1)) #memoiz
            result2 = has_sum(sum, x*orig_n1, (y+1)*orig_n2, x, y+1)
        return result1 or result2
    has_sum.memoiz = set()
    orig_n1, orig_n2 = n1, n2
    return has_sum(sum, n1, n2)