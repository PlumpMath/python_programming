def reverse_list_iter(s):
    """Reverse the contents of the list s and return None.
    
    >>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
    >>> reverse_list_iter(digits)
    >>> digits
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> d = digits
    >>> reverse_list_iter(d)
    >>> digits
    [6, 2, 9, 5, 1, 4, 1, 3]
    """
    length = len(s)
    for index in range( len(s) // 2):
        s[index], s[-index - 1] =  s[-index - 1], s[index]

def reverse_list_recur(s, index = 0):
    """Reverse the contents of the list s and return None.
    
    >>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
    >>> reverse_list_recur(digits)
    >>> digits
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> d = digits
    >>> reverse_list_recur(d)
    >>> digits
    [6, 2, 9, 5, 1, 4, 1, 3]
    """
    if index < len(s) // 2:
        s[index], s[-index - 1] = s[-index - 1], s[index]
        reverse_list_recur(s, index + 1)