def cartesian_product(tup_1, tup_2):
    """Returns a tuple that is the cartesian product of tup_1 and tup_2
	
	>>> X = (1, 2)
	>>> Y = (4, 5)
	>>> cartesian_product(X, Y)
	((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
    """
    new_tuple = ()
    for itup_1 in tup_1:
        for itup_2 in tup_2:
            if itup_1 != itup_2:
                new_tuple += ((itup_1, itup_2),(itup_2, itup_1), )
            else:
                new_tuple += ((itup_1, itup_2), )
    return new_tuple

def cartesian_product_recursive(tup_1, tup_2):
    """Returns a tuple that is the cartesian product of tup_1 and tup_2
	
	>>> X = (1, 2)
	>>> Y = (4, 5)
	>>> cartesian_product(X, Y)
	((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))
    """
    length1 = len(tup_1)
    length2 = len(tup_2)
    def product(tup_1, tup_2, index1, index2):
        if index1 == length1:
            return ()
        elif index2 == length2:
            return product(tup_1, tup_2, index1 + 1, 0)
        else:
            return ((tup_1[index1], tup_2[index2]),) + ((tup_2[index2], tup_1[index1]), ) + product(tup_1, tup_2, index1, index2 + 1)
    return product(tup_1, tup_2, 0, 0)

def cartesian_product_recursive1(tup_1, tup_2):
    res = ((tup_1[0], tup_2[0]), (tup_2[0], tup_2[1]))
    if len(tup_2) == 1:
       return res
    res += cartesian_product_recursive1(tup_1[:1], tup_2[1:])
    if len(tup_1) == 1:
       return res
    res += cartesian_product_recursive1(tup_1[1:], tup_2)
    return res
	
    
        
X = (1, 2, 3)
Y = (4, 5, 6)
result = cartesian_product_recursive1(X, Y)
