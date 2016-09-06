def even_digits(n):
    """Return the percentage of digits in n that are even.

    >>> even_digits(23479837) # 3 / 8
    0.375
    """
    def find_percentage_of_even_digits(n, count_even = 0, count = 0):
        if n == 0:
            return "{0} even digits out of {1} digits".format(count_even, count)
        if (n % 2) == 0:
            return find_percentage_of_even_digits(n // 10, count_even + 1, count + 1)
        else:
            return find_percentage_of_even_digits(n // 10, count_even, count + 1)
    assert n != 0, "Wrong input"
    return find_percentage_of_even_digits(n)