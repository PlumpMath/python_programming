# Sequences are ordered collections of values that support element-selection and have length.
# List is a built-in sequence
# A sequence has a finite length

# A sequence has an element corresponding to any non-negative integer index less than its 
# length, starting at 0.

# Python’s lists are really variable-length arrays, not Lisp-style linked lists.
# The implementation uses a contiguous array of references to other objects, and keeps a pointer
# to this array and the array’s length in a list head structure.
# This makes indexing a list a[i] an operation whose cost is independent of the size of the list
# or the value of the index.
# When items are appended or inserted, the array of references is resized. Some cleverness is 
# applied to improve the performance of appending items repeatedly; when the array must be grown,
# some extra space is allocated so the next few times don’t require an actual resize.

odds = [41, 43, 45, 47]
len(odds)
odds[0]
[2, 7] + [1, 8, 2, 8] * 2    # [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
pairs = [[10, 20], [30, 40]]
pairs[1]
pairs[1][0]

def count_using_while(s, value):
    """Count the number of times that value occurs
    in sequence s
    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_using_for(s, value):
    """Count the number of times that value occurs
    in sequence s
    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def count_pairs(s):
    """Count the number of pairs that occur
    in sequence s
    >>> pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
    >>> count_pairs(pairs)
    2	
    """
    total = 0
	for x, y in s:
        if x == y:
            total = total + 1
    return total


def divisors(n):
    return [1] + [x for x in range(2, n) if n%x == 0]    # n//2 + 1 is the right boundary


# apply_to_all always return lists, no matter what kind of sequence we pass in.
# keep_if will always return lists, no matter what kind of sequence we pass in.

def apply_to_all(map_fn, s):
    """Apply map_fn to each element s
    
    >>> apply_to_all(lambda x : x*3, range(5))
    [0, 3, 6, 9, 12]
    """
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    """List all elements x of s for which filter_fn is true.
    
    >>> keep_if(lambda x: x > 5, range(10))
    [6, 7, 8, 9]
    """
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

apply_to_all(lambda x: x**2, [1, 2, 3, 4])
apply_to_all(lambda a: a, 'cs61a')
keep_if(lambda x: x % 2 == 0, [1, 2, 3, 4])
reduce(lambda a, b: a + b, [1, 2, 3, 4, 5], 0)
reduce(lambda a, b: b + a, 'hello world!', '')
apply_to_all(lambda x: x // abs(x), [1, 3, -1, -4, 2])
keep_if(lambda x: x // 7 % 2 == 0, [1, 7, 14, 21, 28, 35, 42])
reduce(lambda x, y: y + x, 'hello', '')
reduce(lambda x, y: x + y, apply_to_all(lambda s: s + 'a', 'nnnnn'), '') + ' batman!'
