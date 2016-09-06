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
        if lst1[0] <= lst2[0]:
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
    if lst1[0] <= lst2[0]:
        return [lst1[0]] + merge_recur(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge_recur(lst1, lst2[1:])

def mergesort_recur(seq):
    """Mergesort algorithm.

    >>> mergesort_recur([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort_recur([])     # sorting an empty list
    []
    >>> mergesort_recur([1])   # sorting a one-element list
    [1]
    """
    if not seq:
        return []
    if(len(seq) == 1):
        return [seq[0]]
    middle = len(seq) // 2
    left = mergesort_recur(seq[0:middle])
    right = mergesort_recur(seq[middle:len(seq)])
    return merge_recur(left, right)

def middle(seq):
    return len(seq) // 2

def mergesort_iter(seq):
    """Mergesort algorithm.

    >>> mergesort_iter([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort_iter([])     # sorting an empty list
    []
    >>> mergesort_iter([1])   # sorting a one-element list
    [1]
    """
    if not seq:
        return []
    if len(seq) == 1:
        return seq
    def helper():
        partition_boundary_list = []
        partition_copy = seq  		
        while len(partition_copy) > 1:
            partition_boundary_list +=   [[     [0, middle(partition_copy), False],     [middle(partition_copy), len(partition_copy), False]     ]]
            partition_copy = partition_copy[0:middle(partition_copy)]
        list_index = len(partition_boundary_list) - 1
        left_memoiz = -1
        right_memoiz = -1		
        while partition_boundary_list:
            partition_boundary_element = partition_boundary_list[list_index]
            left_lower, left_upper, sorted_left = partition_boundary_element[0]
            right_lower, right_upper, sorted_right =  partition_boundary_element[1]
            if left_lower == left_memoiz:          #Using left_memoiz to check, if already sorted
                partition_boundary_list[list_index][0][2] = True
            if right_upper == right_memoiz:        #Using right_memoiz to check, if already sorted
                partition_boundary_list[list_index][1][2] = True

            if left_upper - left_lower > 1 and  (not partition_boundary_list[list_index][0][2]):
                mid = (left_lower + left_upper) // 2
                partition_boundary_list +=  [[    [left_lower, mid, False],     [mid, left_upper, False]    ]]
                list_index += 1 
            elif right_upper - right_lower > 1 and (not partition_boundary_list[list_index][1][2]):  
                mid = (right_lower + right_upper) // 2
                partition_boundary_list += [[     [right_lower, mid, False],     [mid, right_upper, False]     ]]
                list_index += 1			
            else:
                left_memoiz = left_lower
                right_memoiz = right_upper
                ret_seq = merge_iter(seq[left_lower:left_upper], seq[right_lower:right_upper])
                for element in ret_seq:    # copy sorted sequence
                    seq[left_lower] = element
                    left_lower += 1
                partition_boundary_list.pop(list_index)
                list_index -= 1
    helper()
    return 	seq