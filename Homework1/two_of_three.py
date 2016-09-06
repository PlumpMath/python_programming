def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest of a, b, c.

	Idea is:
	Given a, b, c
	a < b  and a < c   -> b*b + c*c
	b < a  and b < c   -> a*a + c*c
	c < a and  c < b   -> a*a + b*b

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if (a < b) and (a < c):
        return b*b + c*c
    elif (b < a) and (b < c):
        return a*a + c*c
    else:
        return a*a + b*b