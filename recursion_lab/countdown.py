def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n == 1:
        print(n)
    elif n <= 0:
        return
    else:    
        print(n)
        countdown(n-1)

# Is there an easy way to change countdown to count up instead?

def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    if n == 1:
       print(n)
    elif n <= 0:
        return	
    else:
       countup(n-1)
       print(n)